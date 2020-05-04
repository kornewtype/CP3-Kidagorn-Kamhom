usernameInput = input("Username : ")
passwordInput = input("Password : ")

if usernameInput == ("admin") and passwordInput == "1234":
    print("Done !")
    print("---Welcome to New Type Fire Safety Shop---")
    FA1 = "Smoke Detector"
    FA2 = "Fire Alarm Control Panel"
    FA3 = "Alarm Bell"
    FA1P = int(2500)
    FA2P = int(45000)
    FA3P = int(1600)
    print("1. ",FA1, " : ",FA1P," THB Per EA")
    print("2. ",FA2, " : ",FA2P," THB Per EA")
    print("3. ",FA3, " : ",FA3P," THB Per EA")
    ProductChoose = int(input("Please Select Product No. : "))
    ProductQuantity = int(input("Tell me Your Quantity : "))
    if ProductChoose == 1:
        total1 = int(ProductQuantity)
        print("Total Price for Smoke Detector : ",total1*FA1P)
    elif ProductChoose == 2:
        total2 = int(ProductQuantity)
        print("Total Price for Fire Alarm Control Panel : ",total2*FA2P)
    elif ProductChoose == 3:
        total3 = int(ProductQuantity)
        print("Total Price for Alarm Bell : ",total3*FA3P, " THB")
else:
    print("Sorry! Wrong!! Username or Password")
