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
I choose to use a dictionary to store the abbreviations of each direction, the user's input is used as the key value, and the corresponding direction is the value. According to the user's input, the corresponding direction is read from the dictionary. I did not take "Abbreviations for verbs, directions, and items", so verbs, directions, and items are all It must be full spelling, and no ambiguity has been found so far

A drop verb: 
Paired with get, when there is an item in the inventory, using drop to remove the item from the inventory and add it to the items list in the room at the same time, if there is no item in the inventory to use the drop verb, it will prompt invalid.

Interactions
A boss is set in the last room, you can use the attack verb, if there is a sword in your inventory, you will win the game by defeating the boss, if there is no sword, you will lose the game when you are defeated. You can also choose to escape(go) from this room and look for the sword until you find the sword go back to the boss room and defeat the boss
