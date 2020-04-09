# BMI Classification

height = int(input("Enter height in CM : "))
weight = int(input("Enter weight in KG : "))

bmi = weight / ((height/100) ** 2)

if bmi <= 18.5:
    print("Under Weight")
elif bmi <= 25:
    print("Normal Weight")
else:
    print("Over weight")


