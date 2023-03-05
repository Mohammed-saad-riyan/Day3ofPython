print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1 + name2
name.lower()

t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
total = t + r + u + e

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")
total2 = int(l + o + v + e)

score = str(total) + str(total2)
final_score = int(score)


if final_score <= 10 or final_score >= 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >= 40 and final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")
