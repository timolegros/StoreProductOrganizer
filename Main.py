def onShelves():
    """This function opens the onshelves.txt file and appends the information to a list. The product # and ammount
    in stock is appended to a list. Then the function converts this information into int format and filters the
    products to find those that actually need to be ordered. These are appended to a new list called orderList"""

    # creates the lists to be used and opens the first file
    products = []
    orderList = []
    file = open("onshelves.txt", 'r')

    # Creates a list containing lists that contain the product # and amount in stock in int format
    for lines in file.readlines():
        line = lines.rstrip()
        products.append(line.split('#'))
    for product in range(len(products)):
        for item in range(len(products[product])):
            products[product][item] = int(products[product][item])
    file.close()

    # Using the old list, this creates a new list that contains only the products that need tbo and quantity tbo
    for product in products:
        if product[1] < 50:
            product[1] = 50 - product[1]
            orderList.append(product)

    return orderList


def productName(orderList):
    """This function opens the products.txt file containing the product codes and product names. It then matches the
    product codes from orderList created earlier to the product codes in the new list created when the products.txt
    file was opened. If the product codes match than the product name from the productsList is appended to orderList"""

    productsList = []
    file = open("products.txt", "r")

    # opens file and puts every line into a list stored in another list while converting the product # to an integer
    for lines in file.readlines():
        line = lines.rstrip()
        productsList.append(line.split(';'))
    for product in range(len(productsList)):
        productsList[product][0] = int(productsList[product][0])
    file.close()

    # Matches all product codes of products that need to be ordered and appends the product name
    for products in orderList:
        productID = products[0]
        for item in productsList:
            if item[0] == productID:
                products.append(item[1])

    return orderList


def suppliers(orderList):
    """This function opens the availability.txt file and puts all its information into a list called supplierList.
    Then using this new list, the function filters through the list and appends each line to another new list if and
    only if the product code does not already exist in this new list called multipleSuppliers. If the product code is
    already present in the new list, meaning there is a match, then the function compares the prices of each item and
    appends/removes items according to the prices. The multipleSuppliers list is therefore left with only products for
    the lowest prices."""

    supplierList = []
    multipleSuppliers = []
    count = -1
    file = open("availability.txt", "r")

    # puts suppliers available into a list and converts supplier ID to int and price to float
    for lines in file.readlines():
        line = lines.rstrip()
        supplierList.append(line.split(','))
    for supplier in supplierList:
        supplier[0] = int(supplier[0])
    for item in supplierList:
        item[2] = float(item[2])

    # removes any suppliers that offer the same product as another but at a higher price
    for item in supplierList:
        if not any(item[0] in sublist for sublist in multipleSuppliers):
            multipleSuppliers.append(item)
        else:
            for product in multipleSuppliers:
                if product[0] == item[0]:
                    if item[2] <= product[2]:
                        multipleSuppliers.remove(product)
                        multipleSuppliers.append(item)

    # matches the product codes from orderList to multipleSuppliers and appends the info from multipleSuppliers to orderList
    for item in orderList:
        count += 1
        if any(item[0] in sublist for sublist in multipleSuppliers):
            for product in multipleSuppliers:
                if product[0] == item[0]:
                    orderList[count].append(product[2])
                    orderList[count].append(product[1])

    return orderList

def idontknowyet():


def draw(orderList):
    """This function opens the suppliers.txt file containing the companies phone numbers, name, and address. This info
    is put into a list. If the company phone number matches any of those in orderList then the company name is appended
    to the corresponding item in orderList. The function also formats all the data in orderList to be able to properly
    print the output. The total cost of each ordered product is calculated and append to orderList. Then the phone
    number is properly formatted and finally an astrix is added to the product name of any product whose order quantity
    is greater than 40. The function then filters for highest cost. Finally the function prints/writes all the info
     from orderList in the correct format using string formatting."""

    separator = ('+' + '-'*14 + '+' + '-'*18 + '+' + '-'*8 + '+' + '-'*16 + '+' + '-'*10 + '+')
    totalCost = 0
    highestCost = 0
    highCostSuppliers = []
    supplierNames = []
    supplier = []

    # Matches the company name to their phone numbers already in the list and appends it
    file = open('suppliers.txt', 'r')
    for lines in file.readlines():
        line = lines.rstrip()
        supplierNames.append(line.split(';'))
    for item in orderList:
        for name in supplierNames:
            if item[4] == name[0]:
                item.append(name[1])
    file.close()

    # prepares data for entry into table by calculating cost, formatting phone number, adding astrix to product names
    for item in orderList:
        item.append(item[1]*item[3])
        phoneNumber = item[4]
        totalCost += item[6]
        item[4] = '('+phoneNumber[:3]+')'+' '+phoneNumber[3:6]+' '+phoneNumber[6:10]
        if item[6] > highestCost:
            highestCost = item[6]
        if item[1] > 40:
            item[2] = '*'+item[2]
        string = item[2]
        if len(item[2]) >16 and string[:1] != '*':
            item[2] = string[:16]
        else:
            item[2] = string[:17]
    print(orderList)

    # finds the supplier with the highest total order value and appends the company name, number, and cost to a list
    companyName = []
    someList = []
    cost = 0
    for item in orderList:
        if not item[5] in companyName:
            companyName.append(item[5])
    for item in companyName:
        x = 0
        for product in orderList:
            if product[5] == item:
                x += product[6]
        someList.append(x)
    for item in someList:
        if item >= cost:
            cost = item
    for item in someList:
        if cost == item:
            index = someList.index(item)
            name = companyName[index]
            for y in orderList:
                if name == y[5]:
                    supplier.append(name)
                    supplier.append(y[4])
                    supplier.append(cost)
            highCostSuppliers.append(supplier)

    # prints all of the information contained in orderList
    print(separator)
    print('| Product code | Product Name     |Quantity| Supplier       | Cost     |')
    print(separator)
    for item in orderList:
        print("|{:^14d}|{:^18s}|{:7d} |{:^16s}| ${:7.2f} |".format((item[0]), (item[2]), (item[1]), (item[4]),(item[6])))
    print(separator)
    print('| Total Cost   |                 $  %7.2f|'%(totalCost))
    print('+' + '-'*14 + '+' + '-'*27 + '+')
    for highCostSupplier in highCostSuppliers:
        print('Highest cost: {:s} {:s} [${:0.2f}]'.format((highCostSupplier[0]), (highCostSupplier[1]), (highCostSupplier[2])))



    file = open('orders.txt', 'w')
    file.write(separator)
    file.write('\n| Product code | Product Name     |Quantity| Supplier       | Cost     |')
    file.write('\n'); file.write(separator)
    for item in orderList:
        file.write("\n|{:^14d}|{:^18s}|{:7d} |{:^16s}| ${:7.2f} |".format((item[0]), (item[2]), (item[1]), (item[4]),(item[6])))
    file.write('\n'); file.write(separator)
    file.write('\n| Total Cost   |                 $  %7.2f|'%(totalCost))
    for highCostSupplier in highCostSuppliers:
        file.write('\nHighest cost: {:s} {:s} [${:0.2f}]'.format((highCostSupplier[0]), (highCostSupplier[1]), (highCostSupplier[2])))


def main():
    x = onShelves()
    y = productName(x)
    z = suppliers(y)
    draw(z)


main()

