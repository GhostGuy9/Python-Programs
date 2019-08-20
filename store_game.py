#!/usr/bin/python
#Created by: Daniel R Webster

import random
import os

ran = random.randint
again = ""
goods_bought = ""
play = True
goods = 0
money = 1000
rounds = 0
buy = 0
day = 0
week = 0
year = 0
money_score = 0
score = 0
error = 0
rent = 1
version = "1.1.0"

os.system('cls')

print("Store Game V. ", version)
print("----------------------------------------------------------------")
print("Rulez:")
print("----------------------------------------------------------------")
print("Both Tax and 'Price of Good sold back' will be fixed after setting.")
print("Starting Cash at: " + str(money) + ". Max At Start is 200 Goods with cash.")

tax = input("Tax (Default is - 0.0985): ")
if tax == "":
    tax = 0.0985
else:
    tax = float(tax)


cost = input("Selling Price (Default is $5): ")
if cost == "":
    cost = 5
else:
    cost = float(cost)

again = "buy"

while play:
    goods_bought = 0
    if again == "buy":
        goods_bought = input("Enter Number of Goods to buy and sell ($5 for each unit): ")
    rounds = 0
    again = ""
    if goods_bought == "":
        play = False
    else:
        goods_bought = int(goods_bought)
    goods = goods + goods_bought
    score = score + goods
    if goods_bought*5 > money:
        print("Don't Have Enough Money!")
        goods_bought = 0
    if goods > 0:
        money = money-5*goods_bought
        os.system('cls')
        print("Goods Left at Start:", goods, "|", "Money: $", format(money, '.2f'))
    money = money - 250
    print("Paid 250 for rent.")
    rent = rent - 1

    while goods >= 0 and error != 1 and again == "" and money > 5 or rounds < 7 and error != 1 and again == "" and money > 5:
        if 6 > goods < 15:
            buy = ran(0, int(goods*0.25))
        if 15 < goods > 6:
            buy = ran(0, int(goods*0.1))
        if goods == 2:
            buy = ran(0, int())

        goods = int(goods - buy)
        money = money + (cost*buy) + (cost*buy)*tax
        money_score = money_score + (cost*buy) + (cost*buy)*tax
        rounds = rounds + 1
        day = day + 1
        if day == 365:
            day = 0
            year = year + 1
        print("Year:", year, "|", "Day:", day, "|", "Goods Left:", goods, "|", "Bought:", buy, "|", "Money:", format(money, '.2f'))

        while goods == 0 or rounds == 7 or error == 1:
            again = input("What to do (buy/end game/none)? ")
            if again == "buy":
                error = 0
                break
            if again == "none":
                error = 0
                break
            if again == "end game":
                error = 0
                play = False
                break
            else:
                rounds = 0
                error = 1

    if money <= 5:
        print("Game Over!")
        again = input("Play Again? (Y or N)")
        if again == "N" or again == "n":
            play = False
            break
        if again == "Y" or again == "y":
            os.system(__file__)

    if play == 0:
        true_score = float(format(money_score, '.2f'))
        os.system('cls')
        print("Scores")
        print("----------------------")
        print("Goods Left: ", goods)
        print("Goods Sold: ", score-goods)
        print("----------------------")
        print("Time Spent: ", year, "Year(s) | ", day, "Day(s)")
        print("Tax set to: ", float(tax * 100), "%")
        print("----------------------")
        print("Price for per Good sold: $", cost)
        print("Money Collected: $", format(money_score, '.2f'))
        print("Money Spent: $", score*5-(250*rent))
        print("True Money Score: $", format(true_score - (score * 5), '.2f'))
        print("----------------------")
        print("")
        again = input("Play Again? (Y or N)")
        if again == "Y" or again == "y":
            os.system(__file__)
        if again == "N" or again == "n":
            play = False
            break
