# Small pizza: $15
# Medium pizza: $20
# Large pizza: $25

# Pepperoni for small: +$2
# Pepperoni for medium or large: +$3

# Extra cheese: +$1

print("Welcome to Python Pizza deliveries!")
size = input("What size pizza do you want? S, M, or L? \n")
add_pepperoni = input("Do you want to add pepperoni? Y or N \n")
add_extra_cheese = input("Do you want to add extra cheese? Y or N \n")
price = 0

if size == "S":
    price = 15
elif size == "M":
    price = 20
else:
    price = 25
        
if add_pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

if add_extra_cheese == "Y":
    price += 1


print(f"The total bill is ${price}.")