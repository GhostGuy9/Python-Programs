#!/usr/bin/python
# Created by: Daniel R Webster

import random
import os
import configparser
import json


# Variables
ran = 0
inventory = []
inventory_id = []
again = ""
buy_item = ""
gathered = ""
play = True
debug = False
pay = False
lost = False
temp_Inventory = 0
money = 1000
rounds = 0
buy = 0
day = 0
week = 1
month = 1
year = 1
money_spent = 0
money_gained = 0
error = 0
cycle = 0
iid = 0
version = "2.0"
game = 'store'

# Config Set-up
config = configparser.ConfigParser()
config.read('config.int')
#######################################
items = json.loads(config.get(game, 'items'))
cost = json.loads(config.get(game, 'cost'))
wholesale = json.loads(config.get(game, 'wholesale'))
chances = json.loads(config.get(game, 'chances'))
rent = float(config.get(game, 'rent'))

os.system('cls')

if not debug:
    print("Store Game V.", version)
    print("--------------------------------------------------------------------")
    print("Rulez For Game: ")
    print("--------------------------------------------------------------------")
    print("Both Tax and price of Goods sold back will be fixed once game loads.")

print("Starting Cash at: " + '${:,.2f}'.format(money) + " | Rent is: " + '${:,.2f}'.format(rent))

while len(inventory) < len(items):
    inventory_id.insert(iid, -1)
    inventory.insert(iid, 0)
    iid = iid+1

if debug:
    test = 4
    print("")
    print(items[test])
    print("items in list: " + str(len(items)))
    print(wholesale[test])
    print('${:.2f}'.format(float(wholesale[test])))
    print(cost[test])
    print('${:.2f}'.format(float(cost[test])))
    print('Inventory Check: ' + str(inventory) + '| Number of Items: ' + str(len(inventory)))
    print('Chances: ' + str(chances) + '| Number of Items: ' + str(len(chances)))
    print("")
while True:
    tax = input("Tax (Default is - 0.0985 or 9.85%): ")
    if tax == "":
        tax = 0.0985
        break
    elif tax.isdecimal():
        tax = float(tax)

        again = "buy"
        break
    else:
        print('Try Again')

os.system('cls')

command = "start"

while play and command != 'endgame':

    while command != "again" or again == "buy":
        again = ""

        while cycle < len(items):

            t_Item = str(cycle+1) + ")" + str(items[cycle]).capitalize()
            t_Price = " ---- buy: " + '${:,.2f}'.format(float(wholesale[cycle]))
            t_Sell = " ---- sell: " + '${:,.2f}'.format(float(cost[cycle]))
            t_Inv = ' ---- stock: ' + str(int(inventory[cycle]))

            print(t_Item + t_Inv + t_Price + t_Sell)
            cycle = cycle + 1

        if cycle == len(items):
            print('----------------------------------------------')
            print("Money: " + '${:,.2f}'.format(float(money)) + " | Tax for Customer: " + str(tax*100) + '%')
            print('----------------------------------------------')

            mode = 'buy'

            # TODO Keep it from error-ing after a character is entered instead of a int
            while mode == 'buy':
                buy_item = input("Which item to buy?(\"item #\" \"amount\"): ")

                if buy_item == "done" or buy_item == "":
                    cycle = 0
                    os.system('cls')
                    mode = ''
                    break
                else:
                    buying = buy_item.split()

                    if buying[0].isdigit():
                        item_price = float(wholesale[int(buying[0]) - 1])
                        amount = int(buying[1]) + int(inventory[int(buying[0]) - 1])
                    else:
                        print('INT ERROR - Try Again')
                        break

                if int(buying[0]) <= len(items) and buy_item != "done" and money > item_price*amount > 0 and buying[0].isdigit():

                    inventory.pop(int(buying[0]) - 1)
                    inventory.insert(int(buying[0]) - 1, amount)
                    inventory_id.pop(int(buying[0]) - 1)
                    inventory_id.insert(int(buying[0]) - 1, int(buying[0]) - 1)

                    money = money - (item_price * amount)
                    money_spent = money_spent+(item_price * amount)

                    cycle = 0
                    os.system('cls')
                    break

                if not money > item_price*amount > 0:
                    print('---Over Budget---')

                if debug:
                    print('${:.2f}'.format(money))
                    print(inventory)
                    print(inventory_id)

                if int(buying[0]) > len(items) and buy_item != "done":
                    print("try again")
                    print("---------")

            if mode == '':
                break

    ran_num = 0

    if pay:
        money = money - rent
        print("Rent Paid: " + '${:,.2f}'.format(rent) + " | Money After Rent: " + '${:,.2f}'.format(money))
        pay = False

    while day < 7 and buy_item == "done" or "" and money > 0:
        temp_Inventory = 0

        if money < 0:
            lost = True
            break

        cycle = 0
        while cycle < len(inventory):
            temp_Inventory = temp_Inventory + inventory[cycle]
            cycle = cycle + 1

        if temp_Inventory == 0:
            print('Out Of Stock! Buy More Items!')
            inventory.pop(cycle)
            inventory.insert(cycle, -1)

        cycle = 0

        while money > 0 and temp_Inventory > 0:
            ran = random.choices(inventory_id, weights=inventory, k=7)
            ran_choice = random.randint(0, 6)

            if debug:
                print(ran)
                print(ran[ran_choice])

            ran_num = int(ran[ran_choice])
            income = float(cost[inventory_id[ran_num]])

            if int(inventory[ran_num]) > 10:
                gathered = random.randint(1, 10)
            elif inventory[ran_num] <= 10:
                gathered = random.randint(1, inventory[ran_num])

            if inventory[ran_num] != 0:

                day = day + 1

                money = money + ((income*gathered)+((income*gathered)*tax))
                money_gained = money_gained + ((income*gathered)+((income*gathered)*tax))

                tDay = 'Time: ' + str(year) + 'Y ' + str(month) + "M " + str(week) + 'W ' + str(day) + 'D'
                tItem = ' | Item: ' + str(items[ran_num]).capitalize()
                tSold = ' | Sold: ' + str(gathered)
                tIncome = ' | Income: ' + '${:.2f}'.format(float((income*gathered)+((income*gathered)*tax)))
                tItem_Remain = ' | Left Over: ' + str(inventory[ran_num]-gathered)
                tMoney = ' | Money: ' + '${:,.2f}'.format(float(money))

                temp_Amount = inventory[ran_num]

                inventory.pop(ran_num)
                inventory.insert(ran_num, temp_Amount-gathered)

                if inventory[ran_num] == 0:

                    inventory_id.pop(ran_num)
                    inventory_id.insert(ran_num, 0)

                print(tDay + tItem + tSold + tItem_Remain + tIncome + tMoney)

                if debug:
                    print(inventory)
                    print(inventory_id)

                break

            if day == 7:
                break

        ran_num = 0

    if day == 7:
        day = 0
        week = week+1
    if week == 5:
        pay = True
        week = 1
        month = month+1
    if month == 13:
        month = 1
        year = year+1

    if lost:
        print('Bankrupt')
        print('You Lost')
        break

    mode = 'command'

    while mode == 'command':
        cycle = 0
        command = input('What do you want to do(again|buy|endgame)? ')

        if command == 'buy':
            buy_item = ''
            again = 'buy'
            os.system("cls")
            mode = ''
            cycle = 0
            break

        if command == 'again':

            cycle = 0
            while cycle < len(inventory):
                temp_Inventory = inventory[cycle]

                if 0 < temp_Inventory <= 10 and inventory_id[cycle] != -1:
                    print(f"Low on stock for {str(items[cycle]).capitalize()}, Maybe try buying more.")
                    cycle = 0
                    break

                if 0 < temp_Inventory <= 10 and inventory_id == -1:
                    cycle = cycle + 1

                if debug:
                    print("--------------------------")
                    print('ID:', inventory_id[cycle])
                    print('TEMP INV: ', temp_Inventory)
                    print("LOOP #: ", cycle)
                    print("--------------------------")

                if cycle != len(inventory):
                    cycle = cycle + 1

                if cycle == len(inventory):
                    break

        if command == 'again':
            os.system('cls')
            mode = ''
            break

        if command == 'endgame':
            os.system('cls')
            print('Game Ended')
            print('----------')
            print('Money Spent: ' + '${:,.2f}'.format(float(money_spent)))
            print('Money Collected: ' + '${:,.2f}'.format(float(money_gained)))
            print('----------')
            mode = ''
            input('Thanks for Playing! (Press Enter to play again)')
            os.system('python storeV2.py')
            break

        if command != 'endgame' or command != 'again' or command != 'buy' or command != '':
            print('ERROR: COMMAND', '"' + command + '"', 'was used')


if debug:
    print('')
    print('Done!')
