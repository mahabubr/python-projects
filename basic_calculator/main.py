def add(x, y):
    return x + y

def subtract(x, y):
    return  x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Can not divide by zero"
    return x / y

def basic_calculator():
    choice = input("Enter choice (1/2/3/4) : ")

    if choice in ['1', '2', '3', '4']:
        x = float(input("Enter first number : "))
        y = float(input("Enter second number : "))

        if choice == '1':
            print(add(x, y))
        elif choice == '2':
            print(subtract(x, y))
        elif choice == "3":
            print(multiply(x, y))
        else:
            print(divide(x, y))
    else:
        print("Invalid input")

if __name__ == "__main__":
    basic_calculator()
