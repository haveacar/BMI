"""BMI weight calculator study"""

uname = input("Please write your name")
weight = int(input("Please write your weight\nin kg-"))
height = float(input("Please write your height\nin m-"))

# Formula BMI (kg/m2)
bmi = weight / height ** 2

"""
Underweight (Unhealthy)	< 18.5
Normal range (Healthy)	18.5 – 22.9
Overweight I (At risk)	23.0 – 24.9
Overweight II (Moderately obese) 25.0 – 29.9
Overweight III (Severely obese)	≥ 30.0
"""
if bmi < 18.5:
    print(f"{uname} your BMI {round(bmi, 2)}\nUnderweight\U0001F60F")
    pass

elif bmi >= 18.5 and bmi < 22.9:
    print(f"{uname} your BMI {round(bmi, 2)}\nNormal range (Healthy)\U0001F600")
    pass

elif bmi >= 23 and bmi < 24.9:
    print(f"{uname} your BMI {round(bmi, 2)}\nOverweight I (At risk)\U0001F60F")
    pass

elif bmi >= 25 and bmi < 29.9:
    print(f"{uname} your BMI {round(bmi, 2)}\nOverweight II (Moderately obese)\U0001F60F")
    pass

else:
   # bmi > 30:
    print(f"{uname} your BMI {round(bmi, 2)}\nOverweight III (Severely obese)\U0001F60F")
    pass

