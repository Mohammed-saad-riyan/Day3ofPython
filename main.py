height = int(input("Enter your height in cm"))
if height >= 180:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age"))
    if age < 12:
        bill = 5
        print("Child ticket are $5.")
    elif age <= 18:
        bill = 7
        print("Youth ticket are $7")
    else:
        bill = 12
        print("Adult ticket are $12")

    photo = input("do you want a photo taken?? Y or N? ")
    if photo == "Y":
        bill += 3

    print(f"Your total bill is ${bill}")

else:
    print("You can't ride the rollercoaster!")
