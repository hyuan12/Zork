import test as actions
import sys
import data as gs
import os

default_map = "map.json"


def main():
    check_start()
    load_map()
    load_room()


def check_start():
    print("                 A game by Hai ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(
        "As an avid traveler, you have decided to visit the Catacombs of America."
        "\nHowever, during your exploration, you find yourself lost."
        "\nYou can choose to walk in multiple directions to find a way out."
        "\nYou should find a fly to eat.")

    print("For a list of commands type 'help'")


def load_room():
    actions.do_look("")
    actions.get_action()


def load_map():
    if len(sys.argv) > 1:
        # If a filename was provided, load the map data from the file
        map_file = sys.argv[1]
        map_data = gs.get_player_data(map_file)

    elif not os.path.exists(gs.player_file):
        # If no filename was provided, use a default map
        map_data = gs.get_player_data(default_map)
    else:
        return None

    # in case room info doesn't contain key "items"
    for item in map_data:
        if gs.room_items not in set(item.keys()):
            item[gs.room_items] = []

    # create a default player map, then all the changes will happen on this map
    gs.save_player_data({"cur_room": 0, "inventory": [], "map": map_data}, gs.player_file)
    return map_data


if __name__ == '__main__':
    main()
