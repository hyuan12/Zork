# Zork
Hai Yuan   hyuan12

[GitHub Pages](https://github.com/hyuan12/Zork)

20h

**a description of how you tested your code:**

1) I mainly tested my code by manual testing, which means test the code manually by running the program and providing different inputs to see if the expected outputs are produced. For example, I'm gonna "get" a rose form the room, then check the player's map if the rose disappeared. After that, I "drop" the rose and see if the rose put back in the room.

2) Asked a friend of mine to play this game and he gave me some constructive advice.

**any bugs or issues you could not resolve**

***an example of a difficult issue or bug and how you resolved***

At first I wrote all the classes and functions in adventure.py and put all the baseline functionality code into a loop that reads player input, then it got really messy and hard to explain. For ease of understanding, I divided the code into three parts: adventure.py (the program entry is responsible for loading prompts and maps), actions.py (responsible for handling user events) and data.py (responsible for obtaining and setting game data). The overall logic becomes clearer and easier to maintain

***a list of the three extensions you’ve chosen to implement***
Directions become verbs: 
I choose to use a dictionary to store the abbreviations of each direction, the user's input is used as the key value, and the corresponding direction is the value. According to the user's input, the corresponding direction is read from the dictionary. 
```
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
```
I did not take "Abbreviations for verbs, directions, and items", so verbs, directions, and items are all It must be full spelling, and no ambiguity has been found so far


A drop verb: 
Paired with get, when there is an item in the inventory, using drop to remove the item from the inventory and add it to the items list in the room at the same time, if there is no item in the inventory to use the drop verb, it will prompt invalid.
```
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

    gs.weapon = False if(item == "sword") else True
```
Interactions
A boss is set in the last room, you can use the attack verb, if there is a sword in your inventory, you will win the game by defeating the boss, if there is no sword, you will lose the game when you are defeated. You can also choose to escape(go) from this room and look for the sword until you find the sword go back to the boss room and defeat the boss
```
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
```
