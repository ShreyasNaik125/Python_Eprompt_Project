#this code is written by Shreyas Naik (aka website banane waala)

def welcometext():
    print("** HealthyTimes health and fitness club **")
    print("")

def padding():
    print("")

welcometext()

name = input("enter your name => ")
membership_code = int(input("enter membership code => "))
padding()
print("""
    Available meal plans =>
    Type A = 250rs/day
    Type B = 350rs/day
""")
padding()
meal_plan = input("choose a meal plan = > ")
meal_plan_validity = int(input("enter no. of days for which you want to opt for meal plan => "))

if membership_code == 1:
    if meal_plan in ['TYPE A','type a','Type A','type A']:
        discount = 10/100*250
        bill_amount = (250 - discount)*meal_plan_validity
        print(f"your bill is rs {bill_amount}")
    
    elif meal_plan in ['TYPE B','type b','Type B','type B']:
        discount = 15/100*350
        bill_amount = (350 - discount)*meal_plan_validity
        print(f"your bill is rs {bill_amount}")

elif membership_code == 2:
    if meal_plan in ['TYPE A','type a','Type A','type A']:
        discount = 15/100*250
        bill_amount = (250 - discount)*meal_plan_validity
        print(f"your bill is rs {bill_amount}")
    
    elif meal_plan in ['TYPE B','type b','Type B','type B']:
        discount = 20/100*350
        bill_amount = (350 - discount)*meal_plan_validity
        print(f"your bill is rs {bill_amount}")

elif membership_code == 3:
    if meal_plan in ['TYPE A','type a','Type A','type A']:
        discount = 20/100*250
        bill_amount = (250 - discount)*meal_plan_validity
        print(f"your bill is rs {bill_amount}")
    
    elif meal_plan in ['TYPE B','type b','Type B','type B']:
        discount = 25/100*350
        bill_amount = (350 - discount)*meal_plan_validity
        print(f"your bill is rs {bill_amount}")

else:
    exit()
        