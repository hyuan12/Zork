import data as gs
import sys


def do_go(words):
    if len(words) < 1:
        print("Sorry, you need to 'go' somewhere.")
        return
    # get current room info
    dirs = gs.get_direction(words[0])
    if dirs is None:
        print("That direction was not recognized")
        return

    exits = gs.get_cur_room_exit()
    direction = gs.get_direction(words[0])
    if not direction:
        print("That direction was not recognized.")
        return
    if direction not in exits.keys():
        print(f"There's no way to go {direction}.")
        return

    # Move player to new room and save changes to local
    player_data = gs.get_player_data(gs.player_file)
    player_data[gs.u_room_no] = exits[direction]
    gs.save_player_data(player_data, gs.player_file)
    print(f"You go {direction}.\n")
    gs.print_room_info(gs.get_cur_room_info())


def do_help(words):
    gs.print_help()


def do_look(words):
    # Show description of current room
    player_data = gs.get_player_data(gs.player_file)
    cur_room_no = player_data[gs.u_room_no]
    gs.print_room_info(player_data[gs.u_map][cur_room_no])


def do_inventory(words):
    # Show player's inventory
    inv = gs.get_player_inv()
    if not inv:
        print("You're not carrying anything.")
    else:
        print("Inventory:")
        for item in inv:
            print(f"  {item}")


def do_get(words):
    if len(words) < 1:
        print("Sorry, you need to 'get' something.")
        return

    # Check if item is present in current room
    items = gs.get_cur_room_item()
    item = words[0]

    if item not in items:
        print(f"There's no {item} anywhere.")
        return

    # Add item to player's inventory and remove from room
    player_data = gs.get_player_data(gs.player_file)
    player_data[gs.u_map][gs.get_cur_room_number()][gs.room_items].remove(item)
    player_data[gs.u_inv].append(item)
    gs.save_player_data(player_data, gs.player_file)
    print(f"You pick up the {item}.")

    gs.weapon = item == gs.precious


def do_drop(words):
    if len(words) < 1:
        print("Sorry, you need to 'drop' something.")
        return

        # Check if player is carrying specified item
    inv = gs.get_player_inv()
    item = words[0]
    if item not in inv:
        print(f"You're not carrying {item}.")
        return

    # Remove item from player's inventory and add to room
    player_data = gs.get_player_data(gs.player_file)
    player_data[gs.u_inv].remove(item)
    player_data[gs.u_map][gs.get_cur_room_number()][gs.room_items].append(item)
    gs.save_player_data(player_data, gs.player_file)
    print(f"You drop {item}.")

    gs.weapon = False if(item == gs.precious) else True


def do_quit(words):
    print("Goodbye!")
    sys.exit(0)


def do_attack(words):

    if gs.get_cur_room_number() != len(gs.get_player_map()) - 1:
        print("There is nothing to fight with")
        return

    if gs.weapon:
        print("You kill the ghoul with the sword you found earlier. After moving forward, you find one of the "
              "exits. Congrats!")
    else:
        print("The ghoul-like creature has killed you.")
    sys.exit(0)


actions = {
    "go": do_go,
    "help": do_help,
    "look": do_look,
    "inventory": do_inventory,
    "get": do_get,
    "drop": do_drop,
    "quit": do_quit,
    "attack": do_attack,
}


def get_action():
    while True:
        # print("What would you like to do?")
        u_input = ""
        try:
            u_input = input("What would you like to do? ").lower().strip()
        except KeyboardInterrupt:
            do_quit("")
        except EOFError:
            print("Use 'quit' to exit.")
            continue

        if not u_input:
            print("Say something...")
            continue
        words = u_input.split(" ")
        if words:
            verb = words[0]
            if verb in actions:
                actions[verb](words[1:])
            # directions become verbs
            elif verb in gs.directions:
                do_go(gs.get_direction(verb))
            elif verb == "^d":
                print("Use 'quit' to exit.")
                continue
            else:
                print("That command was not recognized")

