# Default values for function

# def profile(name, age = 25, language = "python"):
#     print("name: {0}, age: {1}, language: {2}" .format(name, age, language))

# profile("/ian")


# def profile_1(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("name: {0}, age: {0}" .format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# profile_1("Ian", 25, "python", "R", "MATLAB", "MySQL", "SAS")
# profile_1("Seth", 25, "python", "R", "MATLAB", "MySQL", "SAS", "Java")
# profile_1("Tony", 25, "python", "R", " ", " ", " ")

# What if a person can do more than 5 languages? What if a person can only do 2 languages?
# Then it can make an error or it can be very tiring to make a long function
# So we need to use *language in the fuction

# def profile_2(name, age, *language):
#     print("name: {0}\t age: {0}\t" .format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile_2("Seth", 25, "python", "R", "MATLAB", "MySQL", "SAS", "Java")
# profile_2("Tony", 25, "python", "R")


# Global, local variables
# gun = 10
# def army(soldier):
#     global gun # "global" will bring the variable we define in the global
#     gun = gun - soldier
#     print("Reminding gun: {0}" .format(gun))

# army(2)

# gun = 10
# def army(soldier):
#     # gun <--- this will give you an error.
#     gun = gun - soldier
#     print("Reminding gun: {0}" .format(gun))


# def army(soldier):
#     gun = 20 # This will work becauswe we define a local variable inside the function
#     gun = gun - soldier
#     print("Reminding gun: {0}" .format(gun))

# army(9)



# We can also use "return" in the function
# In this case, we have to put gun in def and write gun when you call the function
gun = 10
def army(gun, soldier):
    gun = gun - soldier
    print("Reminding gun: {0}" .format(gun))
    return gun

gun = army(gun, 7)