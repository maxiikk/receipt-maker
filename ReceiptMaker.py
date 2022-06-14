import os.path
print("Receipt Maker 0.1\n")
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
    print("Input price in" + curr + " and then the name of the product or -1 for exit \n-------------------------------------------------\n")
    itemsnum = 0
    price = "0"
    item = "0"
    total = 0
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
            total += float(price)
            price += curr
            prices.append(price)
        
    print("\nMaking the receipt...")
    l = ""
    for a in date:
        if a == '/':
            l += "_"
        else:
            l += a
    filename = store + " " + l + curr + ".txt"
    exists = 0
    if os.path.isfile(filename):
        f = open(filename, 'a')
        exists = 1
    else:
        f = open(filename, 'w')
    
    if exists == 1:
        f.seek(0, 2)
        with open(filename, "r") as fr:
            lines = fr.readlines()
            pos = 1
            with open(filename, "w") as fw:
                for line in lines:
                    if pos == 5:
                        line = line.replace("Total Cost: ", "")
                        line = line.replace("\n", "")
                        line = float(line)
                        line += total
                        fw.write("Total Cost: " + str(line) + curr + "\n")
                    else:
                        fw.write(line)
                    pos+=1
    else:
        f.write("                  Receipt\n-----------------------------------------------\nDate: " + date + "\nStore: " + store + "\nTotal Cost: " + str(total) + "\n\n")
    i = 0
    for a in items:
        f.write("Product: " + a + "\nPrice: " + str(prices[i]) + "\n\n")
        i += 1
    f.close()
    print("Done!")

exit = 1
while exit == 1:
    makereceipt()
    exit = int(input("type 1 to make another receipt\n"))