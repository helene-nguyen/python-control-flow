height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / height**2)

if bmi < 18.5:
    print(f"According to your BMI which is {bmi}, your are underweight!")
elif bmi < 25:
    print(f"According to your BMI which is {bmi}, your have a normal weight!")
elif bmi < 30:
    print(f"According to your BMI which is {bmi}, your are overweight!")
elif bmi < 35:
    print(f"According to your BMI which is {bmi}, your are obese!")
else:
    print(f"According to your BMI which is {bmi}, your are clinically obese!")
        
