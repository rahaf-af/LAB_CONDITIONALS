wieght=int(input("inter your wieght"))
height=int(input("inter your height"))

BMI=wieght/height**2

if BMI<18.5:
    print("You are underweight. Watch your health")
elif BMI<=24.9 and BMI>=18.5:
    print("You are fit & healthy")
else:
    print("You are overwieght you need to work out more and watch your diet")