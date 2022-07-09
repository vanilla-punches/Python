class BigNumberError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    print("This calculator can only use single digit numbers")
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("input numbers : {0}, {1}".format(num1, num2)) # We can use this when we need to make an intentional error
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("Only single digit numbers are allowed")
except BigNumberError as err:
    print("Error: enter single digit numbers")
    print(err)
finally:
    print("Thank you. Calculator is turned off")