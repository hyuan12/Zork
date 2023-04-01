import getter_setter as gs
import sys

player_file = "player.json"
weapon = False


def go(words):
    if len(words) < 1:
        print("Sorry, you need to 'go' somewhere.")
        return
        # get current room info
    dirs = get_direction(words[1])
    if dirs is None:
        print("That direction was not recognized")
        return

    exits = gs.get_cur_room_exit()
    direction = get_direction(words[1])
    if not direction:
        print("That direction was not recognized.")
        return
    if direction not in exits.keys():
        print("You can't go that way!")
        return

    # Move player to new room and save changes to local
    player_data = gs.get_player_data(player_file)
    player_data[gs.u_room_no] = exits[direction]
    gs.save_player_data(player_data, player_file)
    print(f"You go {direction}.")
    gs.print_room_info(gs.get_cur_room_info())


def do_help():
    gs.print_help()


def look():
    # Show description of current room
    player_data = gs.get_player_data(player_file)
    cur_room_no = player_data[gs.u_room_no]
    gs.print_room_info(player_data[gs.u_map][cur_room_no])


def inventory():
    # Show player's inventory
    inv = gs.get_player_inv()
    if not inv:
        print("You're not carrying anything.")
    else:
        print("Inventory:")
        for item in inv:
            print(f"  {item}")


def get(words):
    if len(words) < 1:
        print("Sorry, you need to 'get' something.")
        return

    # Check if item is present in current room
    psm = gs.get_player_data(player_file)
    items = gs.get_cur_room_item()
    item = words[1]

    if item not in items:
        print(f"There's no {item} here.")
        return

    # Add item to player's inventory and remove from room
    items.remove(item)
    psm[gs.u_inv].append(item)
    gs.save_player_data(psm, player_file)
    print(f"You pick up {item}.")

    global weapon
    weapon = item == "sword"


def drop(words):
    if len(words) < 1:
        print("Sorry, you need to 'drop' something.")
        return

        # Check if player is carrying specified item
    inv = gs.get_player_inv()
    item = words[1]
    if item not in inv:
        print(f"You're not carrying {item}.")
        return

    # Remove item from player's inventory and add to room
    play_data = gs.get_player_data(player_file)
    play_data[gs.u_inv].remove(item)
    play_data[gs.u_room_no][gs.room_items].append(item)
    gs.save_player_data(play_data, player_file)
    print(f"You drop {item}.")

    global weapon
    weapon = False if(item == "sword") else True


def do_quit():
    print("Goodbye!")
    sys.exit(0)


def attack():
    if not weapon:
        print("You can't win with your bare hands")
        return
        # set the boss in the last room
    elif gs.get_cur_room_number() != len(gs.get_player_map()) - 1:
        print("There is nothing to fight with")
        return

    if weapon:
        print("You kill the ghoul with the sword you found earlier. After moving forward, you find one of the "
              "exits. Congrats!")
    else:
        print("The ghoul-like creature has killed you.")
    sys.exit(0)


actions = {
    "go": go,
    "help": do_help,
    "look": look,
    "inventory": inventory,
    "get": get,
    "drop": drop,
    "quit": do_quit,
    "attack": attack,
}


def get_action():
    while True:
        print("What would you like to do?")
        try:
            user_input = input("-> ").lower().strip()
        except KeyboardInterrupt:
            do_quit()
        except EOFError:
            print("Use 'quit' to exit.")
            continue

        words = user_input.split(" ")
        if words:
            verb = words[0]
            if verb in actions:
                actions[verb](words[1:])
            else:
                print("That command was not recognized")
        else:
            print("Say something...")


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
