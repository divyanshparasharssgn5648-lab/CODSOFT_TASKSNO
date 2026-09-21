def calculator():
    print("-----------------------------------")
    print("       SIMPLE PYTHON CALCULATOR    ")
    print("-----------------------------------")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("-----------------------------------")

    while True:
        choice = input("Enter choice (1/2/3/4) or 'q' to quit: ")

        if choice.lower() == 'q':
            print("Exiting calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numerical values only.\n")
                continue

            if choice == '1':
                result = num1 + num2
                print(f"Result: {num1} + {num2} = {result}\n")

            elif choice == '2':
                result = num1 - num2
                print(f"Result: {num1} - {num2} = {result}\n")

            elif choice == '3':
                result = num1 * num2
                print(f"Result: {num1} * {num2} = {result}\n")

            elif choice == '4':
                if num2 == 0:
                    print("Error! Division by zero is not allowed.\n")
                else:
                    result = num1 / num2
                    print(f"Result: {num1} / {num2} = {result}\n")
        else:
            print("Invalid Operation Choice! Please select from 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    calculator()