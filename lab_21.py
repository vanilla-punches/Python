try:
    print("This calculator can only use one digit numbers")
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError # We can use this when we need to make an intentional error
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("Only one digit numbers are allowed")