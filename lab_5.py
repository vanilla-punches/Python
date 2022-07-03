cabinet = {3:"Ian", 28:"Lilly"}
print(cabinet[3])
print(cabinet[28])
print(cabinet.get(3))
# print(cabinet[10]) # If number is not assigned in cabinet function, this will give you an error
print(cabinet.get(10)) # Even though number is not assigned, its result will give "none"
print(cabinet.get(10, 'Available Number'))

print(3 in cabinet) #true
print(19 in cabinet) #false

# Adding new one
cabinet1 = {"A-3":"Leah", "B-3":"Jackie"}
print(cabinet1["A-3"])
cabinet1["C-99"] = "Haze"
print(cabinet1)

# printing only keys
print(cabinet1.keys())

# printing only values
print(cabinet1.values())

# printing both keys and values
print(cabinet1.items())

# Deleting existing keys and values
del cabinet1["B-3"]
print(cabinet1)

# Deleting cabinet
cabinet1.clear()
print(cabinet1)

# tuple: It's like a list but you can't add or remove. However, it's much faster than list
menu = ("Steak", "Bacon")
print(menu[0])
print(menu[1])
# menu.add("Salad") <--- This will give an error

name = "Ted"
age = 25
major = "Math"
print(name, age, major) # This is a list, so you can add or remove

(country, city, post_code) = ("Canada", "Toronto", 361831)
print(country, city, post_code) # This is a tuple

# Set : no repetition and no order
set1 = {5,4,87,2,8,1,10,1,5,5,5,99}
print(set1)

# Intersection
python = {"Ian", "Scott", "Amy", "Sam"}
MySQL = set(["Ian", "Amy", "Daisy"])
print(python & MySQL)
print(python.intersection(MySQL))

# Union
print(python | MySQL)
print(python.union(MySQL))

# Select a programmer who can do MySQL but not python
print(MySQL - python)

python.add("Poppy")
print(python)

python.remove("Sam")
print(python)


cafe = {"Americano", "Latte", "Tea", "Water"} # set ---> {}
print(cafe, type(cafe))
cafe = list(cafe) # list ---> []
print(cafe, type(cafe))
cafe = tuple(cafe)
print(cafe, type(cafe)) # tuple ---> ()