num1 = int(input("enter a number: "))
num2 = int(input("enter a numer : "))

print("1. addition")
print("2. substraction")
print("3. multiplication")
print("4. division") 

choice = int(input("what uh want :"))
match choice :
    case 1 :
        print(f"addation of {num1} and {num2} is {num1 + num2}")
    case 2 :
        print(f"substraction of {num1} and {num2} is {num1 - num2}")
    case 3 :
        print(f"multiplication of {num1} and {num2} is {num1 * num2}")   
    case 4 : 
        if(num2!=0) :
            print(f"division of {num1} and {num2} is {num1 / num2}")
        else :
            print(f"division is not possible")
    case _:
        print("invalid")


