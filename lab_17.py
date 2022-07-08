class unit:
    def __init__(self):
        print("unit producer")

class flyable:
    def __init__(self):
        print("flyable producer")

class flyableunit(unit, flyable):
    def __init__(self):
        # super().__init__()
        unit.__init__(self)
        flyable.__init__(self)

dropship = flyableunit()

# super() ---> when you use mutiple classes, super() will __init__ the last class. For example, flyable class will be ___init___
# if you want to bring both classes, then you need to call each class such as unit.__init__(self) and flyable.__init__(self)