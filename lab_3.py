# How to add a particular numbers, strings, and characters

# Method 1
print("I am %d years old" %20) # %d for numbers
print("I love %s" %"Python") # %s for strings, number
print("Apple start with %c" %"A") # %c for character
print("I like both %s and %s" %("blue","yellow"))

# Method 2
print("I am {} years old" .format(20))
print("I like both {} and {}" .format("blue","yellow"))
print("I like both {1} and {3}" .format("blue","yellow","red","green","white"))

# Method 3
print("I am {age} years old and I like {color}" .format(age = 20, color = "purple"))

# Method 4
age = 99
color = "orange"
print(f"I am {age} years old and I like {color}")


# \n is for changing lines
print("I am studying statistics \nbut I love finance too")
# \
print("I am driving \"BMW\" M3 competition") # use \"\" in order to use " "
# \\  is to use \ in the sentence
print("cdrive\\mycomputer\\python\\project")
# \r is to move something to the front
print("Cafe Latte\rMocha")
# \b is to remove a letter
print("Redd\bMango")
# \t is for tab")
print("Red \tMango")


# www.instagram.com
insta = "http://instagram.com"
address = insta.replace("http://","")
print(address)
address = address[:address.index(".")] # From the entire address, we are going to slice when we see the frist "."
print(address)
password = address[0:4] + str(len(address)) + str(address.count("a")) + "!"
print(password)

print("the password of {social} is {pw}" .format(pw = password, social = address))