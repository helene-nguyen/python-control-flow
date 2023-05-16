print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# true love
lower_name1 = name1.lower()
lower_name2 = name2.lower()

combined_string = lower_name1 + lower_name2

t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")

true = t + r + u + e 

l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")

love = l + o + v + e

love_score = str(true) + str(love)
score_to_int = int(score)

if score_to_int < 10 or score_to_int > 90:
    print(f"Your score is {score}, you go together like coke and mentos!")
elif score_to_int >= 40 and score_to_int <= 50:
    print(f"Your score is {score}, you are alright together!")
else:
    print("Your score is {score}.")