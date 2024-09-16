weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in meters:"))

height_in_meters = height / 100
BMI = weight / (height_in_meters**2)
print(BMI)

if(BMI < 18.5):
    print("You are Underweight"),BMI

elif(18.5 <= BMI <24.9):
    print("You are Normal weight"),BMI

elif(25 <= BMI < 29.9):
    print("You are Overweight"),BMI

elif(BMI >= 29.9):
    print("You are Obesity"),BMI
