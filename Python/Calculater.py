def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def power(a, b):
    return a ** b
def modulus(a, b):
    if b == 0:
        raise ValueError("Cannot perform modulus with zero.")
    return a % b
def floor_divide(a, b):
    if b == 0:
        raise ValueError("Cannot perform floor division by zero.")
    return a // b
def main():
    print("========= Calculator =========")
    print("Addition:", add(2, 3))
    print("Subtraction:", subtract(5, 2))
    print("Multiplication:", multiply(4, 3))
    print("Division:", divide(10, 2))
    print("Power:", power(2, 3))
    print("Modulus:", modulus(10, 3))
    print("Floor Division:", floor_divide(10, 3))
    choice=int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for power, 6 for modulus, 7 for floor division: "))
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    if choice==1:
        print("Result:", add(num1, num2))
    elif choice==2:
        print("Result:", subtract(num1, num2))  
    elif choice==3:
        print("Result:", multiply(num1, num2))
    elif choice==4:
        try:
            print("Result:", divide(num1, num2))
        except ValueError as e:
            print(e)
    elif choice==5:
        print("Result:", power(num1, num2))
    elif choice==6:
        try:
            print("Result:", modulus(num1, num2))
        except ValueError as e:
            print(e)
    elif choice==7:
        try:
            print("Result:", floor_divide(num1, num2))
        except ValueError as e:
            print(e)
    else:
        print("Invalid choice.")
if __name__ == "__main__":
    main()