year = int(input("Which year do you want to check? \n"))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(f"This year {year} is a leap year!")
        else:
            print(f"This year {year} is not a leap year!")
    else:
        print(f"This year {year} is a leap year!")
else:
    print(f"This year {year} is not a leap year!")