products = [
    {"name": "Shirt", "price": 10, "stock": 20},
    {"name": "Hat", "price": 5, "stock": 30},
    {"name": "Pants", "price": 7, "stock": 16},
]
while True:
    print("")
    print("Welcome to the menu")
    print("1. View Products")
    print("2. Search Product")
    print("3. Add Product")
    print("4. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        for product in products:
            print(product["name"], "-", product["price"], "USD, stock:", product["stock"])
    elif choice == 2:
        while True:
            print("1. Search product by name")
            print("2. Pick from list")
            print("3. Return to the main menu")
            method = int(input("Select an option: "))
            if method == 1:
                search = input("Enter the product name: ")
                found = False
                for product in products:
                    if search.lower() == product["name"].lower():
                        print(product["name"], "-", product["price"], "USD, stock:", product["stock"])
                        found = True
                if found == False:
                    print("Product not found")
            elif method == 2:
                while True:
                    print("Remaining options: ")
                    for i in range(len(products)):
                        print(str(i+1) + "." + products[i]["name"])
                    print(str(len(products)+1) + ".Exit")
                    selection = int(input("Please select the available option:"))
                    if selection >= 1 and selection <= len(products):
                        product = products[selection - 1]
                        print(product["name"], "-", product["price"], "USD, stock:", product["stock"])
                    elif selection == len(products)+1:
                        print("Return to the search menu")
                        break
            elif method == 3:
                print("Return to the main menu")
                break
    elif choice == 3:
        newitem = input("Add the new product: ")
        newprice = float(input("Enter the new price:"))
        newstock = int(input("Enter the new stock:"))
        products.append({"name": newitem, "price": newprice, "stock": newstock})
        print(f"{newitem}" " got added")
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again")