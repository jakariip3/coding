try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    else:
        print("Invalid operation.")
        raise Exception

    print("Result:", result)

    try:
        file = open("calculator.txt", "a")
        file.write(f"{op}, {num1}, {num2}, {result}\n")
        file.close()
    except Exception:
        print("Error writing to file.")

except ValueError:
    print("Please enter numbers only.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
except Exception:
    print("Something went wrong.")
