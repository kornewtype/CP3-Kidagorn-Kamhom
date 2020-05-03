usernameInput = input("Username : ")
passwordInput = input("Password : ")

if usernameInput == ("admin") and passwordInput == "1234":
    print("Done !")
    print("---New Type---")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    userSelected = int(input("input : 1 for admin or 2 for Co-Admin : "))
    if userSelected == 1:
        price = int(input("Price (THB) : "))
        vat = 7
        result = int(price + (price*vat/100))
        print(result)
    elif userSelected == 2:
        price1 = int(input("First Product Price : "))
        price2 = int(input("Second Product Price : "))
        print(price1+price2)

