# Regular Unit
from re import U
from random import *


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} Unit has just produced".format(name))

    def move(self, location):
        print("[Ground Unit Move]")
        print("{0} : Moving toword {1} with speed of {2}".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : got {1} damaged".format(self.name, damage))
        self.hp -= damage
        print("{0} : current hp is {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : Unit is destroyed".format(self.name))

# Attcking Unit
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : Attacking enemy at {1} direction with damage {2}".format(self.name, location, self.damage))

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "Marine", 40, 1, 5)
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : stimpack is used HP is reduced by 10".format(self.name))
        else:
            print("{0} : HP is too low. Can't use stimpack".format(self.name))

class Tank(AttackUnit):
    seize_developed = False
    def __init__(self):
        AttackUnit.__init__(self, "Tank", 150, 1, 35)
        self.seize_mode = False
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        if self.seize_mode == False:
            print("{0} : Seize mode completed".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0} : Seize mode released".format(self.name))
            self.damage /= 2
            self.seize_mode = False

# Flyable Class
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{0} : Flying toword {1} [Speed: {2}]".format(name, location, self.flying_speed))

# Flyable Unit
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "Wraith", 80, 20, 5)
        self.clocked = False
    def clocking(self):
        if self.clocked == True:
            print("{0} : Clocking mode removed".format(self.name))
        else:
            print("{0} : Clocking mode on".format(self.name))
            self.clocked = True


def game_start():
    print("[Notice] Game begins")
def game_over():
    print("Player: gg")
    print("[Player] left the game")

game_start()
    
m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)


for unit in attack_units:
    unit.move("North east")
    

Tank.seize_developed = True
print("Seized Mode is completed")

# Ready for attack
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Wraith):
        unit.clocking()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()

# Attack
for unit in attack_units:
    unit.attack("North East")

# Damaged randomly
for unit in attack_units:
    unit.damaged(randint(5, 21))

game_over()