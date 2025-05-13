# Randomization + validation of user input algo - Sebas
from random import randint

def Digging_holes(inventory, holes_dug_today): 
        example_json_common = {"common":["potato", "trash", "soda","grape"]}
        example_json_rare = {"rare":["potato", "trash", "soda","grape"]}
        example_json_super_rare = {"super_rare":["potato", "trash", "soda","grape"]}
        example_json_legendary = {"legendary":["potato", "trash", "soda","grape"]}
        example_json_rarity2 = {"potato":2, "trash": 3, "soda":6, "grape":5}
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
                    list_value = randint(0, 3)
                    key = item_list[list_value]
                    while (key in inventory ):
                        list_value = randint(0, 3)
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
                    return inventory, holes_dug_today

# data about user
user = { 
    "money" : 150,
    "inventory" : []
}
# shop data
shop = {
        "banana" : 5,
        "apple" : 2,
        "gem" : 50
}

def buy(money, inventory, item):
    price = shop[item]
    if price is None:
        return f"Item '{item}' was not found in shop."
    if money < price:
        return f"Not enough money for {item}."
    if item in inventory:
        return f"You already own {item}."
    
    confirm = input(f"Item: {item}, Price: ${price}. Confirm purchase? (y/n):")
    if confirm.lower() != "y":
        return "Purchase canceled."

    inventory.append(item)
    money -= price
    return f"{item} has been bought. Current balance: ${user['money']}"

def sell(money, inventory, item):
    if item not in inventory:
        return f"{item} is not in inventory. Unable to sell."
    
    confirm = input(f"Selling {item} for ${price}. Confirm sell? (y/n):")
    if confirm.lower() != "y":
        return "Sale canceled."
    
    price = shop.get(item, 0)
    money += price
    inventory.remove(item)
    return f"{item} was sold! Current balance: ${user['money']}"

# add healthbar and healthbar data - ian
#global values that will be changed/moved later
current_hunger = 50
max_hunger = 100
def eat(food_item):
    global current_hunger

    if not isinstance(food_item, dict) or 'name' not in food_item or 'restore' not in food_item:
        print("Invalid food item.")
        return

    restored = food_item['restore']
    current_hunger += restored
    current_hunger = min(current_hunger, max_hunger)

    print(f"You ate {food_item['name']} and restored {restored} hunger.")
    print(f"Current hunger: {current_hunger}/{max_hunger}")
# create json file + find more specific algorithm - Seun
# Deducts rent from the player's money at the end of each day.
def rent(player_money, rent_amount, day_number, eviction_day=7):
    if player_money >= rent_amount:
        player_money -= rent_amount
        eviction_status = False
        print(f"Paid ${rent_amount} in rent. Remaining: ${player_money}")
    else:
        eviction_status = (day_number == eviction_day)
        player_money -= rent_amount
        print(f"Couldn't pay full rent! You now have ${player_money}")
        if eviction_status:
            print("Eviction day! You are evicted.")
        else:
            print("Not enough money for rent, but not eviction day yet.") 
               
    return player_money, eviction_status
# where the program runs from-sebas
def main():
    inventory = {}
    holesdug = 1
    playersmoney = 0
    day = 0
    didyoulose = False
    print("You're living as an unsuccessful farmer. Your crops have been \
neglected and you need money! Your last resort digging holes on your farm! Sell\
the items you find to pay your rent!!!")
    while True:
        answer = input("Please select an option \n[1] Dig a hole?\
\n[2] Sell your items?\
\n[3] Eat some food?\
\n[4] Sleep for the day\n")
        try: 
            int(answer)
        except ValueError:
            print("unfortunately your input is not a int try again")
            continue
        else:
            answer = int(answer)
            if(answer < 1 or answer > 4):
                print("unfortunately you have not choosen a number 1-4")
        if (answer == 1):
            if (holesdug == 3):
                print("unfortunately you have no more digs left for the day")
                continue
            inventory,holesdug = Digging_holes(inventory, holesdug)
            
        
        elif (answer == 2):
            print (f"Your current inventory is {inventory}")
            print (f"The items avaliable to buy are {shop}")
            while (True):
                buying = input("if you would like to buy an item select 1 if \
you if you would like to sell an item select 2 if you wish to exit select 3?\
\n[1] Buy a item?\n[2] Sell your items?\n[3] exit?\n")
                try: 
                    int(buying)
                except ValueError:
                    print("unfortunately your input is not a int try again")
                    continue
                else:
                    buying = int(buying)
                    if(buying < 1 or buying > 3):
                        print("unfortunately you have not choosen a number 1-3")
                if (buying == 1):
                    whattobuy = input("What do you want to buy?\n")
                    print(buy(whattobuy))
                elif (buying == 2):
                    whattosell = input("What do you want to sell?\n")
                    print(sell(whattosell))
                else:
                    break
        elif (answer == 3):
             while (True):
                 print(f"You're current hunger level is at {current_hunger}")
                 eating = input("if you would like to eat some food select 1 if \
you if you would like to exit select 2?\
\n[1] Eat some food?\n[2] exit?\n")
                 try: 
                    int(eating)
                 except ValueError:
                    print("unfortunately your input is not a int try again")
                    continue
                 else:
                    eating = int(eating)
                    if(eating < 1 or eating > 2):
                        print("unfortunately you have not choosen a number 1-2")
                 if (eating == 1):
                    whattoeat = input("what item do you want to eat?\n")
                    print(eat(whattoeat))
                 else:
                    break
             
                     
                
        else:
            holesdug = 1
            if (playersmoney > 299):
                print("You did it you raised enough money to buy the land!!!")
                print("CONGRATS!!!")
                break
            else:
                playersmoney, didyoulose = rent(playersmoney, 15, day)
                if (didyoulose == True):
                    print("unfortunately your land was taken better luck next\
 time")
                    break
                elif (playersmoney < 15):
                    print(f"You've gone into debt! you have {7-(day+1)} days\
 remaining to get 300$")
                    day += 1
                else:
                    print(f"rent was payed for today! you have {7-(day+1)} days\
 remaining to get 300$")
                    day += 1


if __name__ == "__main__":
    main()