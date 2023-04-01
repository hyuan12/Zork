"""This is the character module, it stores information on the character and items."""

double_word_list = ["fish_sticks", "key_hook", "front_door", "bedroom_door"]

character_inventory = []
current_room = None

def print_inventory():
    if len(character_inventory) < 1:
        print("Your pockets are empty! Wait, how do frogs have pockets?")
    else:
        print("--INVENTORY--")
        for item in character_inventory:
            print("-" + item)

# This could get tedious for every item in the game, look for an alternative solution?
def get_description(item, form):
    item_dict = {
        "pamphlet": pamphlet,
        "fish_sticks": fish_sticks,
        "key": key,
        "lantern": lantern,
        "photo": photo,
        "jar": jar
    }

    ob = item_dict.get(item, lambda: "ERROR")

    try:
        if form == "read":
            return ob.read_description
        elif form == "examine":
            return ob.exam_description
    except AttributeError:
        return "There's nothing to see of importance."

use_on_items ={
    "key": "door"
}


class Items:
    def __init__(self, read_desc, exam_desc):
        self.read_description = read_desc
        self.exam_description = exam_desc

pamphlet = Items("The flies future is YOUR Future. Donate today!",
                 "This is an annoying pamphlet, it came in the mail")
fish_sticks = Items("MOPI Brand Fish Sticks! Unethically sourced, deep fried fun!",
                    "These fish sticks are LONG expired, and unethically sourced at that. Better leave them be.")
key = Items("34TH BURROW STREET",
            "It's an old cast iron key, it's been in your family for generations.")
lantern = Items("",
                "It's a trusty oil lamp. It provides plenty of light, and was just recently topped off.")
photo = Items("Forever yours and always :) Jan. 10, 1993",
              "It's a wedding photo of your Aunt Frogatha and Uncle Frogert. They're posing in front of the pond, "
              "many flies can be seen buzzing in the background. There's something written on the back.")
jar = Items("",
            "It is an empty glass jar.")