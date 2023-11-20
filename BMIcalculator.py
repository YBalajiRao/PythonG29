H = float(input("Enter your height in meters: "))
W = float(input("Enter your weight in kilograms: "))
gender = input("Enter your gender (male/female): ")

the_BMI = W / (H ** 2)
print("BMI Calculated is:", the_BMI)

if the_BMI > 0:
    if gender == 'MALE' or gender == 'male':
        if the_BMI <= 18.5:
            print("You are underweight")
        elif the_BMI <= 25:
            print("Congrats! You are healthy")
        elif the_BMI <= 30:
            print("You are overweight")
        else:
            print("You are obese")
    elif gender == 'FEMALE' or gender == 'female':
        if the_BMI <= 18.5:
            print("You are underweight")
        elif the_BMI <= 24:
            print("Congrats! You are healthy")
        elif the_BMI <= 29:
            print("You are overweight")
        else:
            print("You are obese")
    else:
        print("Invalid gender entered., pls enter MALE  or FEMALE" )
else:
    print("Enter valid details")
