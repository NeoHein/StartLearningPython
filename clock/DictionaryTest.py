# !/usr/bin/python3
# Mini Mart Store Program
# Programmer : PMH
# Version : 0.0.1
# Date : 7/2/2021

items = [0, 'Communication', 'Daily_use', 'Stationary']
Communication = ["Handset", "Keypad", "PC", "Laptop", "Radio"]
Daily_use = ["HandWatch", "T-shirt", "style-pant", "Cap", "Hat", "Shoes", "Slippers"]
Stationary = ["Ball-pen", "Pencil", "Eraser", "Paper", "Book", "Calculator", "Ruler"]
C = {"#": 0, "Handset": 250, "Keypad": 20, "PC": 300, "Laptop": 400, "Radio": 10}
D = {"#": 0, "HandWatch": 50, "T-shirt": 8, "style-pant": 20, "Cap": 8, "Hat": 8, "Shoes": 30, "Slippers": 15}
S = {"#": 0, "Ball-pen": 1, "Pencil": 1, "Eraser": 1, "Paper": 1, "Book": 2, "Calculator": 10, "Ruler": 1}
while True:
    print()
    print()
    print("There are three types of items:")
    print()
    print("1: Communication  2: Daily use  3: Stationary")
    print()
    item_type = int(input("Please Choose the Items as You Want: "))
    print()
    if items[item_type] in items:
        print("You selected: ", items[item_type])
    else:
        print("Wrong Choice! We have only 3 item types. Try again later.")
    print()
    if items[item_type] == items[1]:
        print("We have following Communication Devices:")
        print()
        print(Communication)
    elif items[item_type] == items[2]:
        print("We have following Daily_use Devices:")
        print()
        print(Daily_use)
    elif items[item_type] == items[3]:
        print("We have following Stationary Devices:")
        print()
        print(Stationary)
    else:
        print("Error! Try again")
    print()
    selected_item = input("Enter the item name you want to buy!: ")
    print()
    if selected_item in C:
        print("You selected: ", selected_item, " & It's ", C[selected_item], "$")
    elif selected_item in D:
        print("You selected: ", selected_item, " & It's ", D[selected_item], "$")
    elif selected_item in S:
        print("You selected: ", selected_item, " & It's ", S[selected_item], "$")
    else:
        print("Error! Try again")
    print()
    print()
    input_ = int(input("Press 0 to Exit & Press 1 to Continue: "))
    if input_ == 0:
        print()
        print("Exiting.....")
        break
    else:
        print()
        print("Restarting The Process.....")
        continue
