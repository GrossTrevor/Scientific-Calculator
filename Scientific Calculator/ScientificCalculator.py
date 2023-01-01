import math

value = float(0)
valList = []
choice = -1

while choice != 0:
    print(f"Current Result: {value}")
    print("\nCalculator Menu")
    print("---------------")
    print("0. Exit Program")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Logarithm")
    print("7. Display Average")
    choice = int(input("\nEnter Menu Selection: "))

    if choice > 7 or choice < 0:
        while choice > 7 or choice < 0:
            print("Error: Invalid selection.")
            choice = int(input("\nEnter Menu Selection: "))

    if choice == 7:
        while choice == 7:
            if len(valList) == 0:
                print("Error: No calculations yet to average!")
            else:
                total = 0
                for x in valList:
                    total += x
                print(f"\nSum of calculations: {total}")
                print(f"Number of calculations: {len(valList)}")
                print(f"Average of calculations: {round(total / len(valList), 2)}")

            choice = int(input("\nEnter Menu Selection: "))
    if choice == 0:
        print("Thanks for using this calculator. Goodbye!")
        break

    temp = input("Enter first operand: ")
    if temp == "RESULT":
        first = value
    else:
        first = float(temp)
    temp = input("Enter second operand: ")
    if temp == "RESULT":
        second = value
    else:
        second = float(temp)

    if choice == 1:
        value = first + second
    if choice == 2:
        value = first - second
    if choice == 3:
        value = first * second
    if choice == 4:
        value = first / second
    if choice == 5:
        value = first ** second
    if choice == 6:
        value = math.log(first, second)
    valList.append(value)
    print("")