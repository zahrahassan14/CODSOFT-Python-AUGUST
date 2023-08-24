operation = int(input("What operation do you wish to perform?\n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide \n"))
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


if operation == 1:
    output = num1 + num2
    print("The sum of the two numbers is:  ", output)


elif operation == 2:
    output = num1 - num2
    print("The difference between the two numbers is: ",output)


elif operation == 3:
    output = num1 * num2
    print("The product of the two numbers is:  ", output)


elif operation == 4:
    if num2 == 0:
        print("Indivisible by zero!")
    else:
        output = num1 / num2
        print("The division of the two numbers is:  ", output)


else:
    print("Invalid Choice")
