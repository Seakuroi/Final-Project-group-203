# Randomization + validation of user input algo - Sebas
from random import randint

def Digging_holes(): 
        # for now inventory will be empty but this will be an argument later
        inventory = {}
        example_json_common = {"common":["potato", "trash", "soda"]}
        example_json_rare = {"rare":["potato", "trash", "soda"]}
        example_json_super_rare = {"super_rare":["potato", "trash", "soda"]}
        example_json_legendary = {"legendary":["potato", "trash", "soda"]}
        example_json_rarity2 = {"potato":2, "trash": 3, "soda":6}
        holes_dug = []
        holes_dug_today = 1
        while True:
            hole = input("There are ten holes select a hole you would like to \
dig : " )
            try: 
                int(hole)
            except ValueError:
                print("unfortunately your input is not a int try again")
                continue
            else:
                hole = int(hole)
                if(hole < 1 or hole > 10):
                    print("unfortunately the hole you picked is not \
a number between 1 and 10. \n Please try again")
                    continue
                if (hole in holes_dug):
                    print("unfortunately the hole you picked has \
already been dug for the day. \n Please try again")
                    continue
            if ((hole >= 1 and hole <= 10) and hole not in\
                holes_dug):
                item_value =  randint(0, 100)
                if (item_value <= 65):
                    item_list = example_json_common["common"]
                    # this range will be adjusted for items 
                    list_value = randint(0, 2)
                    key = item_list[list_value]
                    while (key in inventory ):
                        list_value = randint(0, 2)
                        key = item_list[list_value]
                    inventory[key] = example_json_rarity2[key]
                    print(f"You have just recived a {key}, it is currently \
valued at {inventory[key]}$")
                elif(item_value <= 90):
                    item_list = example_json_rare["rare"]
                    list_value = randint(0, 2)
                    key = item_list[list_value]
                    while (key in inventory ):
                        list_value = randint(0, 2)
                        key = item_list[list_value]
                    inventory[key] = example_json_rarity2[key]
                    print(f"You have just recived a {key}, it is currently \
valued at {inventory[key]}$")
                elif(item_value <= 99):
                    item_list = example_json_super_rare["super_rare"]
                    list_value = randint(0, 2)
                    key = item_list[list_value]
                    while (key in inventory ):
                        list_value = randint(0, 2)
                        key = item_list[list_value]
                    inventory[key] = example_json_rarity2[key]
                    print(f"You have just recived a {key}, it is currently \
valued at {inventory[key]}$")
                else:
                    item_list = example_json_legendary["legendary"]
                    list_value = randint(0, 2)
                    key = item_list[list_value]
                    while (key in inventory ):
                        list_value = randint(0, 2)
                        key = item_list[list_value]
                    inventory[key] = example_json_rarity2[key]
                    print(f"You have just recived a {key}, it is currently \
valued at {inventory[key]}$")
                if (holes_dug_today == 1):
                    print("You have 2 more digs remaining")
                    holes_dug.append(hole)
                    holes_dug_today += 1
                    continue
                elif (holes_dug_today == 2):
                    print("You have 1 more dig remaining")
                    holes_dug.append(hole)
                    holes_dug_today += 1
                    continue
                else:
                    print("You have no more digs remaining go sell your items\
 at the shop!!!")
                    print (f"Your current inventory is {inventory}")
                    return inventory
        
if __name__ == "__main__":
    Digging_holes()
# sebas
# New idea about shop in-game - can't use user input - Aminata
# add healthbar and healthbar data - ian
# create json file + find more specific algorithm - Seun
