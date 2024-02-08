def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def calculator():
    print("Welcome to Simple Calculator!")
    
    while True:
        print("\nOperations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        try:
            choice = int(input("Enter operation choice (1/2/3/4): "))
            if choice not in [1, 2, 3, 4]:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a valid operation choice (1/2/3/4).")
            continue
    
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue
        
        if choice == 1:
            print("Result:", add(num1, num2))
        elif choice == 2:
            print("Result:", subtract(num1, num2))
        elif choice == 3:
            print("Result:", multiply(num1, num2))
        elif choice == 4:
            print("Result:", divide(num1, num2))
        
        continue_choice = input("\nDo you want to continue? (yes/no): ").lower()
        if continue_choice != "yes":
            print("Thank you for using the calculator!")
            break

if __name__ == "__main__":
    calculator()
1