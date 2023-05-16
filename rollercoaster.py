print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))
child_ticket = 5
youth_ticket = 7
adult_ticket = 12
total_price = 0

if height > 120:
    print("You can ride the rollercoaster!")
    age= int(input("What is your age ? "))
    
    if age < 12:
        print(f"Child ticket price is ${child_ticket}.")
        total_price = child_ticket
    elif age <= 18:
        print(f"Youth ticket price is ${youth_ticket}.")
        total_price = youth_ticket
    elif age >= 45 and age <=55:
        total_price = 0  
    else:
        print(f"Adult ticket price is ${adult_ticket}.")
        total_price = adult_ticket
    
    ask_photo = input("Would you like a photo? (yes/no) \n")
    if ask_photo == "yes":
        total_price += 3
        print(f"Ok, the total price is ${total_price}.")
    else:
        print(f"Ok, the total price is ${total_price}.")
        
else:
    print("Sorry, you have to grow taller before you can ride.")