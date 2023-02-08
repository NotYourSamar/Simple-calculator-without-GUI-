# Calculator but one time function

# function to add two numbers.
def add(x,y):
    return x+y

# function to substract two numbers.
def substract(x,y):
    return x-y

# function to multiply two numbers.
def multiply(x,y):
    return x*y

#function to power a numbers.
def powerof(x,y):
    return x**y

#function to divide two numbers
def divide(x,y):
    return x/y

print("Select What You Want to do by selecting 1 , 2 , 3 , 4 & 5 from the listed operations")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Powering")
print("5. Division")

while True:
    lmao = input("Enter What You Want to do :")
    if lmao in ('1','2','3','4','5'):
        try:
            number1 = float(input("Enter Your First Number :"))
            number2 = float(input("Enter Your Second Number :"))
        except ValueErr:
            print("Invalid Input!")
            continue
        if lmao == "1":
            print(f"{number1} + {number2} =", add(number1, number2))
        elif lmao == "2":
            print(f"{number1} - {number2} =", substract(number1, number2))
        elif lmao == "3":
            print(f"{number1} * {number2} =", multiply(number1, number2))
        elif lmao == "4":
            print(f"{number1} ** {number2} =", powerof(number1, number2))
        elif lmao == "5":
            print(f"{number1} / {number2} =", divide(number1, number2))
        chutiya = input("Do You Want To Do Calculations Further (yes/no)")
        if chutiya == "no":
            break
    else:
        print("Invalid Input! Please Provide a Number between 1 - 5")
