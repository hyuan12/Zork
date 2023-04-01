import actions
import sys

default_map = "map.json"


def main():
    check_start()
    load_map()
    load_room()


def check_start():
    print("                 A game by Hai ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(
        "You are in a burrow, but not just any burrow. The burrow you reside in is in fact"
        "\nthe estate of Von Frogerick III, who just so happens to be your great great grandfather."
        "\nThe immense and fascinating history of your lineage matters not though, for you are hungry."
        "\nYou should find a fly to eat.")

    print("For a list of commands type 'h', '?', 'help'")


def load_room():
    actions.get_action()


def load_map():
    if len(sys.argv) > 1:
        # If a filename was provided, load the map data from the file
        map_file = sys.argv[1]
        map_data = actions.get_player_data(map_file)
    else:
        # If no filename was provided, use a default map
        map_data = actions.get_player_data(default_map)

    # in case room info doesn't contain key "items"
    for item in map_data:
        if actions.room_items not in set(item.keys()):
            item[actions.room_items] = []

    # create a default player map, then all the changes will happen on this map
    base_dic = {"cur_room": 0, "inventory": [], "map": map_data}

    actions.save_json(base_dic, actions.player_file)
    return map_data


# if __name__ == '__main__':
#     main()
