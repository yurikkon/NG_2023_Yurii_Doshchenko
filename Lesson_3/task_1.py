def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Choise operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter number operaton (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

match choice:
    case  '1':
        print(num1, "+", num2, "=", add(num1, num2))

    case  '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    case  '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    case  '4':
        print(num1, "/", num2, "=", divide(num1, num2))