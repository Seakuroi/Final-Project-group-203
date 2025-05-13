# Randomization + validation of user input algo - Sebas
from random import randint
import matplotlib.pyplot as plt
def Digging_holes(inventory, holes_dug_today): 
        common_dictionary = {"common":["paper", "water bottle","can",\
"scrap metal","plastic","rock","dirt","feather","shell","sticker","beer bottle"\
,"boot","worm","candy wrapper","paper towel","trash","beetle","spider","hair\
 clip","grass","hay"]}
        rare_dictionary = {"rare":["soda", "beer", "coin","marble","action \
figure","hat","bone","tooth","key chain","pen","lighter","pin","25$ dollars",\
"sandel","shirt"]}
        super_rare_dictionary = {"super_rare":["Gold ring", "silver coin",\
"camera","watch","ruby","fossile","gun","coin jar","painting"]}
        legendary_dictionary = {"legendary":["iphone", "treasure map", \
"diamond","200$ bill", "oil reserve"]}
        example_json_rarity2 = {"paper":4, "water bottle":4,"can":4,\
"scrap metal":5,"plastic":5,"rock":5,"dirt":5,"feather":6,"shell":6,"sticker":6\
,"beer bottle":7,"boot":7,"worm":7,"candy wrapper":7,"paper towel":7,"trash":7,\
"beetle":8,"spider":8,"hair clip":9,"grass":10,"hay":10,"soda":15, "beer":15, \
"coin": 15,"marble": 15,"action figure":17,"hat":17,"bone":17,"tooth":19,"key \
chain":20,"pen":20,"lighter":22,"pin":22,"25$ dollars":25,"sandel":25,"shirt"\
:25,"Gold ring":40, "silver coin":43,"camera":43,"watch":45,"ruby":50,"fossile"\
:55,"gun":60,"coin jar":66,"painting":70,"iphone":120, "treasure map":150, \
"diamond":180,"200$ dollars":200, "oil reserve":250}
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
                empty_hole = randint(1,10)
                item_value = "none" if hole == empty_hole else randint(0, 100)
                if item_value == "none":
                    print("Nothing in this hole :(")
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
                        print("You have no more digs remaining go sell your\
items at the shop!!!")
                        print (f"Your current inventory is {inventory}")
                    return inventory, holes_dug_today
                elif (item_value <= 65):
                    item_list = common_dictionary["common"]
                    # this range will be adjusted for items 
                    list_value = randint(0, 20)
                    key = item_list[list_value]
                    while (key in inventory ):
                        list_value = randint(0, 20)
                        key = item_list[list_value]
                    inventory[key] = example_json_rarity2[key]
                    print(f"You have just recived a {key}, it is currently \
valued at {inventory[key]}$")
                elif(item_value <= 90):
                    item_list = rare_dictionary["rare"]
                    list_value = randint(0, 14)
                    key = item_list[list_value]
                    while (key in inventory ):
                        list_value = randint(0, 14)
                        key = item_list[list_value]
                    inventory[key] = example_json_rarity2[key]
                    print(f"You have just recived a {key}, it is currently \
valued at {inventory[key]}$")
                elif(item_value <= 99):
                    item_list = super_rare_dictionary["super_rare"]
                    list_value = randint(0, 9)
                    key = item_list[list_value]
                    while (key in inventory ):
                        list_value = randint(0, 9)
                        key = item_list[list_value]
                    inventory[key] = example_json_rarity2[key]
                    print(f"You have just recived a {key}, it is currently \
valued at {inventory[key]}$")
                elif(item_value <= 100):
                    item_list = legendary_dictionary["legendary"]
                    list_value = randint(0, 4)
                    key = item_list[list_value]
                    while (key in inventory ):
                        list_value = randint(0, 4)
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


# shop data
shop = {
        "banana" : 5,
        "apple" : 2,
        "chicken" : 10,
        "steak" : 20,
        "tuna" : 7,
        "cake" : 30,
        "ice cream" : 13,
        "pasta" : 12,
        "full restore" : 50,
}

def buy(money, inventory, item):
    """Author: Aminata
    Allows user to buy item from shop.

    Args:
    money (int): The player's amount of money.
    inventory (list): The player's inventory.
    item (str): The name of the item the player wishes to buy.

    Returns:
    money (int): The player's updated amount of money.
    inventory (list): The player's updated inventory
    str: Returns messages about the transaction.
    """
    price = shop[item]
    if price is None:
        return f"Item '{item}' was not found in shop.", money
    if money < price:
        return f"Not enough money for {item}.", money
    if item in inventory:
        return f"You already own {item}.",money
    
    confirm = input(f"Item: {item}, Price: ${price}. Confirm purchase? (y/n):")
    if confirm.lower() != "y":
        return "Purchase canceled.",money

    inventory[item] = shop[item]
    money -= price
    return f"{item} has been bought. Current balance: ${money}" ,money

def sell(money, inventory, item):
    """Author: Aminata
    Allows user to sell item from their inventory.

    Args:
    money (int): The player's amount of money.
    inventory (list): The player's inventory.
    item (str): The name of the item the player wishes to sell.

    Returns:
    money (int): The player's updated amount of money.
    inventory (list): The player's updated inventory
    str: Returns messages about the sale.
    """
    if item not in inventory:
        return f"{item} is not in inventory. Unable to sell.",money
    
    price = inventory[item]
    confirm = input(f"Selling {item} for ${price}. Confirm sale? (y/n):")
    if confirm.lower() != "y":
        return "Sale canceled.",money
    money += inventory[item]
    del inventory[item]
    return f"{item} was sold! Current balance: ${money}",money

# add healthbar and healthbar data - ian
#global values that will be changed/moved later

food_items = {
    "banana": {"name": "banana","restore": 3},
    "apple": {"name": "apple","restore": 1},
    "chicken": {"name": "chicken","restore": 6},
    "steak": {"name": "steak","restore": 8},
    "tuna": {"name": "tuna","restore": 4},
    "cake": {"name": "cake","restore": 15},
    "ice cream": {"name": "ice cream","restore": 10},
    "pasta": {"name": "pasta","restore": 9},
    "full restore": { "name": "full restore", "restore": 25}
}


class HungerBar:
    def __init__(self, max_hunger=25, current_hunger=5):
        """Initialize the HungerBar class 
        with the maximum hunger and starting hunger levels.

        Args:
        max_hunger (int): The maximum hunger level, default is 25.
        current_hunger (int): The starting hunger level, default is 5.
        """
        self.max_hunger = max_hunger
        self.current_hunger = current_hunger

    def __call__(self, dug):
        """
        Simulate the passage of one day 
        and decrease hunger accordingly when called.

        Args:
        dug (int): The number of times the user dug during the day. 
                   A value greater than 1 increases hunger loss.

        Returns:
        int: The updated hunger level after the daily loss.
        """
       
        daily_hunger_loss = 5 if dug > 1 else 2
        self.current_hunger -= daily_hunger_loss
        self.current_hunger = max(self.current_hunger, 0)

       
        print(f"A day has passed. Hunger decreased by {daily_hunger_loss}.")
        print(f"Current hunger: {self.current_hunger}/{self.max_hunger}")
        
    
        return self.current_hunger

    def __repr__(self):
        """
        Represent the current state of the hunger simulator.
        
        Returns:
        str: A string representation of the hunger simulator with current hunger status.
        """
        return f"HungerSimulator(current_hunger={self.current_hunger}, max_hunger={self.max_hunger})"
hunger_bar = HungerBar()
hunger_log = []
hunger_log.append(5)
def eat(food_name):
    """Consume a food item to restore hunger based on its name.
    
    Args:
    food_name (str): The name of the food item to consume.
    
    Returns:
    None: Prints the name of the food, amount of hunger restored, 
    and the current hunger level. If the food name is invalid, 
    prints an error message instead.
    """

    if food_name not in food_items:
        print("Food item not found.")
        return

    food_item = food_items[food_name]
    restored = food_item['restore']
    hunger_bar.current_hunger += restored
    hunger_bar.current_hunger = min( hunger_bar.current_hunger, hunger_bar.max_hunger)

    print(f"You ate {food_item['name']} and restored {restored} hunger.")
    print(f"Current hunger: { hunger_bar.current_hunger}/{ hunger_bar.max_hunger}")
    

def plot_hunger_over_time(hunger_log):
    """
    Visualize the hunger level over time using a line plot.

    Args:
    hunger_log (list of int): A list of hunger values recorded at each game step.

    Returns:
    None: Displays a plot of hunger vs. time.
    """
    days = list(range(1, len(hunger_log) + 1))
    plt.figure(figsize=(10, 5))
    plt.plot(days, hunger_log, marker='o', linestyle='-', color='orange')
    plt.title("Hunger Over Time")
    plt.xlabel("Day")
    plt.ylabel("Hunger Level")
    plt.ylim(0, hunger_bar.max_hunger)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    
        
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
\n[2] Buy/Sell items?\
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
                continue
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
                    print (f"The items avaliable to buy are {shop}")
                    whattobuy = input("What do you want to buy?\n")
                    message,money = buy(playersmoney,inventory,whattobuy)
                    print(message)
                    playersmoney = money
                elif (buying == 2):
                    print (f"Your current inventory is {inventory}")
                    whattosell = input("What do you want to sell?\n")
                    message,money = sell(playersmoney,inventory,whattosell)
                    print(message)
                    playersmoney = money
                elif (buying == 3):
                    break
        elif (answer == 3):
             while (True):
                 print(f"You're current hunger level is at { hunger_bar.current_hunger}")
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
                    print (f"Your current inventory is {inventory}")
                    whattoeat = input("what item do you want to eat?\n")
                    print(eat(whattoeat))
                 elif (eating == 2):
                    break
        elif (answer == 4):
            hunger_log.append(hunger_bar(holesdug))
            holesdug = 1
            if (playersmoney > 299):
                print("You did it you raised enough money to buy the land!!!")
                print("CONGRATS!!!")
                break
            elif ( hunger_bar.current_hunger == 0):
                print("unfortunately you starved to death better luck next\
 time!!!\nMaybe try buying food at the shop?")
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
    # Plot hunger over course of game
plot_hunger_over_time(hunger_log)
