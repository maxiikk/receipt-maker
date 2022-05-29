from os import system, name
import os.path
print("Receipt Maker 0.1\n")
'''def clear():
   if name == 'nt':
      _ = system('cls')
   else:
   _ = system('clear')'''
while 1:
    curr = input("Set Currency (E = Euro, D = Dollars, R = Rubles): ")
    if curr.upper() == 'E' or curr.upper() == 'D' or curr.upper() == 'R':
        if curr.upper() == 'E':
            curr = " EUR"
            print("Currency set as:" + curr)
        elif curr.upper() == 'D':
            curr = " USD"
            print("Currency set as:" + curr)
        else:
            curr = " RUB"
            print("Currency set as:" + curr)
        break;
def makereceipt():
    store = input("Store: ")
    date = input("Date (DD/MM/YYYY): ")
    print("Input price in " + curr + " and then the name of the product or -1 for exit \n-------------------------------------------------\n")
    itemsnum = 0
    price = "0"
    item = "0"
    prices = []
    items = []
    while price != "-1" or item != "-1":
        print("Item " + str(itemsnum + 1) + ":")
        item = str(input("Product Name: "))
        if item == "-1":
            break
        else:
            items.append(item)
            itemsnum += 1
        price = str(input("Price: "))
        if price == "-1":
            itemsnum -= 1
            items.pop()
            break
        else:
            price += curr
            prices.append(price)
        
    print("\nMaking the receipt...")
    l = ""
    for a in date:
        if a == '/':
            l += "_"
        else:
            l += a
    filename = store + " " + l + ".txt"
    exists = 0
    if os.path.isfile(filename):
        f = open(filename, 'a')
        exists = 1
    else:
        f = open(filename, 'w')
    
    if exists == 1:
        f.seek(0, 2)
    else:
        f.write("                  Receipt\n-----------------------------------------------\nDate: " + date + "\nStore: " + store + "\n\n")
    i = 0
    for a in items:
        f.write("Product: " + a + "\nPrice: " + str(prices[i]) + "\n\n")
        i += 1
    f.close()
    print("Done!")

makereceipt()

exit = 0
while exit != 1:
    exit = int(input("type 1 for exit"))