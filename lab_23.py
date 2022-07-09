class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1
while(True):
    try:
        print("[Remaining chicken] : {0}".format(chicken))
        order = int(input("How many chicken would you like?"))
        if order > chicken:
            print("Out of stock")
        elif order <= 0:
            raise ValueError
        else:
            print("[Waiting number: {0}] {1} chicken is ready".format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("Wrong order is placed")
    except SoldOutError:
        print("We have no chicken to sell")
        break