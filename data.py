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

weapon = False
precious = "sword"

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


def print_help():
    """
    Print the list of available commands.
    """
    print("--HELP--")
    print("-'go' + object to go in specified direction")
    print("-'look' - provides description of the room")
    print("-'quit' - leaves the game")
    print("-'inventory' - to see what you've got")
    items = get_cur_room_item()
    inv = get_player_inv()
    if items:
        print("-'get' + object to put an object in your inventory")
    if inv:
        print("-'drop' + object to put an object back in the room")
    global weapon
    if weapon:
        print("-'attack' - prepares for a fight")


def print_room_info(room_dict):
    """
    Print the room name, description, items, and exits.
    """
    print(f"\n> {room_dict[room_name]}")
    print(f"\n{room_dict[room_desc]}")
    if room_items in room_dict.keys() and len(room_dict[room_items]) > 0:
        print(f"\nItems: {','.join(room_dict[room_items])}")
    print(f"\nExits: {' '.join(room_dict[room_exits].keys())}\n")


def get_direction(u_input):
    """
    Get the direction based on the user input.
    """
    return directions.get(u_input)
