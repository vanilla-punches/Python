try:
    print("Calculatory [Only Division Allowed]")
    nums = []
    nums.append(int(input("Enter first number : ")))
    nums.append(int(input("Enter second number : ")))
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("There is an error")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("Unknown error")
    print(err)