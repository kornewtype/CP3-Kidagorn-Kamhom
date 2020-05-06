numberInput = int(input("Number Input : "))
space = numberInput
for x in range(numberInput):
    space = space - 1
    text = ""
    for y in range(2*x+1):
        text += "*"
    print(" "*space+text)