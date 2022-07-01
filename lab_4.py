# list []
bus1 = 10
bus2 = 30
bus3 = 80

bus = [10, 30, 70]
print(bus)

bus = ["Jason", "Joe", "Smith"]
print(bus.index("Smith"))

bus.append("Emma") # append() is for adding
print(bus)

bus.insert(1, "Maria") # insert() is to add something before index number
print(bus)

print(bus.pop()) # pop() is to remove from the last
print(bus)
print(bus.pop())
print(bus)

airplane = ["Alex", "Elli", "John", "Jack", "Omar", "John", "John", "Scott"]
print(airplane.count("John"))

number_list = [4,2,5,3,10,2,2,8,5]
number_list.sort()
print(number_list)

number_list.reverse()
print(number_list)

number_list.clear()
print(number_list)

number_list = [4,2,5,3,10,2,2,8,5]
mix_list = ["Harry", 10, True]
print(mix_list)

number_list.extend(mix_list)
print(number_list)