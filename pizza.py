from pizzapy import *
import configparser
import os

#int
order_time = ''

#Config Set-up
config = configparser.ConfigParser()
config.read('config.int')

print('Pizza Py')
print('------------')
start = input('"New" or "Saved" data: ').lower()

if start == 'new':
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter email: ")
    cell_phone = input("Enter Cell Phone #: ")
    address = input("Enter Address: ")
    customer = [first_name+"\n", last_name+"\n", email+"\n", cell_phone+"\n", address+"\n"]

    config.set('pizzapy', 'first_name', first_name)
    config.set('pizzapy', 'last_name', last_name)
    config.set('pizzapy', 'email', email)
    config.set('pizzapy', 'cell_phone', cell_phone)
    config.set('pizzapy', 'address', address)

    with open('config.int', 'w') as configfile:
        config.write(configfile)

    print('Save New Info to Profile...')
elif start == 'saved':

    first_name = config.get('pizzapy', 'first_name')
    last_name = config.get('pizzapy', 'last_name')
    email = config.get('pizzapy', 'email')
    cell_phone = config.get('pizzapy', 'cell_phone')
    address = config.get('pizzapy', 'address')

    print('Load Profile...')
print('Setting Up Order...')

#SetUp for Adding to menu
print('-------------------------------------------------')
person = Customer(first_name, last_name, email, cell_phone, address)
print(person)
print('-------------------------------------------------')
shop = StoreLocator.find_closest_store_to_customer(person)
print(shop)
print('-------------------------------------------------')
order = Order.begin_customer_order(person, shop)
print(order)


#Clears Terminal
os.system('cls')

while not order_time == 'd' or 'done':
    menu = shop.get_menu()

    print('Time to Order')
    print('-------------')
    print('\033[1m'+'A'+'\033[0m'+'dd?')
    print('\033[1m'+'S'+'\033[0m'+'earch?')
    print('\033[1m'+'R'+'\033[0m'+'emove?')
    print('\033[1m'+'D'+'\033[0m'+'one?')
    order_time = input('Select from Above: ').lower()


    if order_time == 'a':
        add = input('Item Code(Add): ')
        order.add_item(add.upper())
    if order_time == 's':
        item = input("Search Item Name: ")
        os.system('cls')
        menu.search(Name=str(item.capitalize()))
    if order_time == 'r':
        remove = input('Item Code(Remove): ')
        order.remove_item(remove.upper())
    if order_time == 'd':
        break
    elif order_time == '':
        print('ERROR')

card_num = input('Please Input card number (Card Number will be saved): ')

config.set('pizzapy', 'card_num', card_num)
with open('config.int', 'w') as configfile:
    config.write(configfile)

answer = input('Would you like to place you order? ').lower()

if answer == 'yes':
    order.place(card_num)
else:
    print('Order Canceled')
