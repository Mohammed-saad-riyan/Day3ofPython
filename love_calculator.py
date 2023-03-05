print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


lower_name = name1.lower()
lower_name2 = name2.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
total = int(t + r + u + e)
t2 = lower_name2.count("t")
r2 = lower_name2.count("r")
u2 = lower_name2.count("u")
e2 = lower_name2.count("e")
total2 = int(t2 + r2 + u2 + e2)
grand_total = int(total + total2)

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
total3 = int(l + o + v + e)
l2 = lower_name2.count("l")
o2 = lower_name2.count("o")
v2 = lower_name2.count("v")
e2 = lower_name2.count("e")
total4 = int(l2 + o2 + v2 + e2)
grand_total2 = int(total3 + total4)

score = str(grand_total) + str(grand_total2)

final_score = int(score)

if final_score <= 10 or final_score >= 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >= 40 and final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")
