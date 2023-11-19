H=float(input("Enter your height in Centimeters: "))
W=float(input("Enter your Weight in Kilograms: "))
 
the_BMI=W/(H/100)**2
print("BMI Calculated is:  ",the_BMI)
 
if(the_BMI>0):
    if(the_BMI<=18.5):
        print("You are underweight")
    elif(the_BMI<=25):
        print("Congrats! You are Healthy")
    elif(the_BMI<=30):
        print("You are overweight")
    else: 
        print("You are Obeset")
else:
    print("enter valid details")