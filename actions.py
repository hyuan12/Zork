import json
import sys

player_file = "player.json"
room_name = "name"
room_exits = "exits"
room_desc = "desc"
room_items = "items"

u_room_no = "cur_room"
u_map = "map"
u_inv = "inventory"
complex_actions = ["go", "look", "get", "drop", "inventory", "quit", "attack"]

weapon = False


def get_action():
    global weapon
    while True:
        print("What would you like to do?")
        # handle unusual exit
        try:
            user_input = input("-> ").lower().strip()
        except KeyboardInterrupt:
            print("Goodbye!")
            sys.exit(0)
        except EOFError:
            print("Use 'quit' to exit.")
            continue

        words = user_input.split(" ")
        if not words:
            print("Say something...")
            continue

        verb = words[0]
        if verb in ('go',):
            if len(words) < 2:
                print("Sorry, you need to 'go' somewhere.")
                continue

            # get current room info
            dirs = get_direction(words[1])
            if dirs is None:
                print("That direction was not recognized")
                continue

            exits = get_cur_room_exit()
            direction = get_direction(words[1])
            if not direction:
                print("That direction was not recognized.")
                continue
            if direction not in exits.keys():
                print("You can't go that way!")
                continue

            # Move player to new room and save changes to local
            psm = get_player_data(player_file)
            psm[u_room_no] = exits[direction]
            save_player_data(psm, player_file)
            print(f"You go {direction}.")
            print_room_info(get_cur_room_info())

        elif verb in ("h", "?", "help"):
            print_help()

        elif verb in ("look", "l"):
            # Show description of current room
            psm = get_player_data(player_file)
            cur_room_no = psm[u_room_no]
            print_room_info(psm[u_map][cur_room_no])

        elif user_input in ("inventory", "i", "inv"):
            # Show player's inventory
            inventory = get_player_inv()
            if not inventory:
                print("You're not carrying anything.")
            else:
                print("Inventory:")
                for item in inventory:
                    print(f"  {item}")

        elif verb in ("get",):
            if len(words) < 2:
                print("Sorry, you need to 'get' something.")
                continue

            # Check if item is present in current room
            psm = get_player_data(player_file)
            items = get_cur_room_item()
            item = words[1]

            if item not in items:
                print(f"There's no {item} here.")
                continue

            # Add item to player's inventory and remove from room
            items.remove(item)
            psm[u_inv].append(item)
            save_player_data(psm, player_file)
            print(f"You pick up {item}.")

            # global weapon
            weapon = item == "sword"

        elif verb in ("drop",):
            if len(words) < 2:
                print("Sorry, you need to 'drop' something.")
                continue

            # Check if player is carrying specified item
            inventory = get_player_inv()
            item = words[1]
            if item not in inventory:
                print(f"You're not carrying {item}.")
                continue

            # Remove item from player's inventory and add to room
            play_data = get_player_data(player_file)
            play_data[u_inv].remove(item)
            play_data[u_room_no][room_items].append(item)
            save_player_data(play_data, player_file)
            print(f"You drop {item}.")

            weapon = False if(item == "sword") else True

        elif verb in ("quit",):
            print("Goodbye!")
            sys.exit(0)

        elif verb in ("attack",):
            if not weapon:
                print("You can't win with your bare hands")
                continue
            # set the boss in the last room
            elif get_cur_room_number() != len(get_player_map()) - 1:
                print("There is nothing to fight with")
                continue

            if weapon:
                print("You kill the ghoul with the sword you found earlier. After moving forward, you find one of the "
                      "exits. Congrats!")
            else:
                print("The ghoul-like creature has killed you.")
            sys.exit(0)
        else:
            print("That command was not recognized")


# Functions
def print_room_info(room_dict):
    """
    Print the room name, description, items, and exits.
    """
    print(f"> {room_dict[room_name]}")
    print(f"\n{room_dict[room_desc]}")
    if room_items in room_dict.keys() and len(room_dict[room_items]) > 0:
        print(f"\nItems: {','.join(room_dict[room_items])}")
    print(f"\nExits: {' '.join(room_dict[room_exits].keys())}")


def save_player_data(data, filename):
    """
    Save the given data to the specified file in JSON format.
    """
    json_object = json.dumps(data, indent=4)
    with open(filename, "w") as f:
        f.write(json_object)


def get_cur_room_item():
    """
    Get the list of items in the current room.
    """
    player_data = get_player_data(player_file)
    current_room_no = player_data[u_room_no]
    return player_data[u_map][current_room_no][room_items]


def get_player_inv():
    """
    Get the list of items in the player's inventory.
    """
    psm = get_player_data(player_file)
    return psm[u_inv]


def get_player_map():
    psm = get_player_data(player_file)
    return psm[u_map]


def get_cur_room_number():
    psm = get_player_data(player_file)
    return psm[u_room_no]


def get_cur_room_info():
    psm = get_player_data(player_file)
    cur_room_no = psm[u_room_no]
    return psm[u_map][cur_room_no]


def get_cur_room_exit():
    cur_room_info = get_cur_room_info()
    return cur_room_info[room_exits]


def get_player_data(filename):
    """
    Load data from the specified file in JSON format.
    """
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (IOError, OSError):
        print("Cannot load game. File not found.")
        return None
    except FileNotFoundError:
        print(f"Could not find file: {filename}")
        return None


def get_direction(user_input):
    """
    Get the direction based on the user input.
    """
    directions = {
        "north": "north",
        "n": "north",
        "south": "south",
        "s": "south",
        "west": "west",
        "w": "west",
        "east": "east",
        "e": "east",
        "northwest": "northwest",
        "nw": "northwest",
        "northeast": "northeast",
        "ne": "northeast",
        "southwest": "southwest",
        "sw": "southwest",
        "southeast": "southeast",
        "se": "southeast",
    }
    return directions.get(user_input)


def print_help():
    """
    Print the list of available commands.
    """
    print("--HELP--")
    print("-'go' + object to go in specified direction")
    print("-'look' - provides description of the room")
    print("-'quit' - leaves the game")
    items = get_cur_room_item()
    inv = get_player_inv()
    if items:
        print("-'get' + object to put an object in the inventory")
    if inv:
        print("-'drop' + object to put an object back in the room")
    global weapon
    if weapon:
        print("-'attack' - prepares for a fight")
