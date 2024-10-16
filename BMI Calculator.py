Weight= float(input("enter you Weight (in kgs): "))
Height= float(input("enter you Height (in meters) : "))

BMI = Weight/(Height**2)

if BMI<18.5:
    print(f"Your BMI is {BMI} , You are under weight")
elif 18.5<=BMI<25:
     print(f"Your BMI is {BMI} , You are normal weight")
elif 25<=BMI:
     print(f"Your BMI is {BMI} , You are Overweight ")
else:
     print("please enter a valid input")
