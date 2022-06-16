import os.path
print("Receipt Maker v0.2\n")
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
    while 1:
        date = input("Date (DD/MM/YYYY): ")
        i = 1
        first = 0
        second = 0
        rights = 0
        num = 0
        days = 0
        dayss = ''
        month = 0
        monthss = ''
        year = 0
        years = ''
        right = [1, 1, 1]
        for a in date:
            if a == '/' and (i == 2 or i == 3):
                for b in range (0, i-1):
                    try:
                        dayss += date[b]
                        days = int(dayss)
                    except:
                        print("Only numbers as days!")
                        right[0] = 0
                        break
                if right[0] == 1:
                    first = i
                    rights += 1
            if a == '/' and (i == 4 or i == 5 or i == 6): # 1/1/2022 = 2 and 4 10/1/2022 = 3 and 5 10/10/2022 = 3 and 6
                if rights == 1:
                    second = i
                    for b in range(first, second-1):
                        try:
                            monthss += date[b]
                            month = int(monthss)
                            if month > 12 or month <= 0:
                                right[1] = 0
                        except:
                            right[1] = 0
                            break
                    if right[1] == 1:
                        rights += 1
                    else:
                        print("Months should be a number and cant be more than 12!")
                    for c in range(second, len(date)):
                        try:
                           years += date[c]
                           year = int(years)
                        except:
                            print("Only numbers as years!")
                            right[2] = 0
                            break
                    if right[2] == 1:
                        if month == 2 and (days > 28 and year%4 != 0):
                            rights = 0
                        elif month == 2 and (days > 29 and year%4 == 0):
                            rights = 0
                        if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month ==12) and days > 31:
                            rights = 0
                        if (month == 4 or month == 6 or month == 9 or month == 11) and days > 30:
                            rights = 0
                        rights+=1
            i += 1
        if rights == 3:
            break;
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
