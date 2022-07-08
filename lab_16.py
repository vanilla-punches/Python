# Class

# Name = "Marine"
# Stemina = 40
# Damage = 5

# print("{0} is produced".format(Name))
# print("Stemina {0}, Damage {1}\n".format(Stemina, Damage))

# Tank_name = "Seige Tank"
# Tank_stemina = 150
# Tank_damage = 35

# print("{0} is produced".format(Tank_name))
# print("Stemina {0}, Damage {1}\n".format(Tank_stemina, Tank_damage))

# def attack(name, location, damage):
#     print("{0} is attacking toward {1} direction. [Damage {2}]".format(name, location, damage))

# attack(Name, "North East", Damage)
# attack(Tank_name, "North East", Tank_damage)


# There are many units will be created. You can't create Tank1, Tank2, Marine1, Marine1, Marine3 every single time.
# So, we should use "Class" to make our life much easier

# Regular unit
class unit:
    def __init__(self, name, stemina, speed):
        self.name = name
        self.stemina = stemina
        self.speed = speed
        # self.damage = damage
        
    def move(self, location):
        print("groun unit is moving")
        print("{0} is moving toward {1} with speed of {2}".format(self.name, location, self.speed))
# # marine1 = unit("marine", 40, 5)
# # marine2 = unit("marine", 40, 5)
# # tank = unit("tank", 150, 35)

# wraith1 = unit("Wraith", 80, 5)
# print("Unit name: {0}, Damage: {1}".format(wraith1.name, wraith1.damage))

# # We can create an external source outside of class
# # class has only name, stemina, and damage, but clocking is one we created outside class
# wraith2 = unit("Lost Wraith", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0} is now clocking mode".format(wraith2.name))


# Attacking Units
class attackunit(unit):
    def __init__(self, name, stemina, speed, damage ):
        # self.name = name
        # self.stemina = stemina
        unit.__init__(self, name, stemina, speed) # Transfering name and stemina class info from "unit" class we made above
        self.damage = damage

    def attack(self, location):
        print("{0} is attacking toward {1} direction. [Damage {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} is damaged by {1}".format(self.name, damage))
        self.stemina -= damage
        print("{0} has {1} stemina".format(self.name, self.stemina))
        if self.stemina <= 0:
            print("{0} is killed".format(self.name))

# firebet1 = attackunit("Firebet", 50, 16, 5)
# # Attack
# firebet1.attack("South East")
# # Damaged
# firebet1.damaged(25)


class flyable:
    def __init__(self, speed):
        self.speed = speed

    def fly(self, name, location):
        print("{0} is moving toward {1} with speed of {2}".format(name, location, self.speed))

class flyableattack(attackunit, flyable):
    def __init__(self, name, stemina, damage, speed):
        attackunit.__init__(self, name, stemina, 0, damage) # ground unit speed 0
        flyable.__init__(self, speed)

    def move(self, location):
        print("fylable unit is moving")
        self.fly(self.name, location)

# valkyrie = flyableattack("Valkyrie", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "East")

# vulture  = attackunit("vulture", 80, 10, 20)
# battlecruiser = flyableattack("Battlecruiser", 500, 25, 3)

# vulture.move = "North West"
# battlecruiser.fly(battlecruiser.name, "West")
# battlecruiser.move("West")


# Building

# Pass function!

# class buildingunit(unit):
#     def __init__(self, name, stemina, location):
#         pass # It just passes

# supply_depot = buildingunit("Supply Depot", 500, "South West")

# def game_start():
#     print("Game has begun")

# def game_over():
#     pass

# game_start()
# game_over()

class buildingunit(unit):
    def __init__(self, name, stemina, location):
        # unit.__init__(self, name, stemina, 0)
        super().__init__(name, stemina, 0) # when you use super(), you don't need to use self in the bracket
        self.location = location