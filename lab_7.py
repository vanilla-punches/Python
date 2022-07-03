# if function

# weather = input("What is today's weather?")
# if weather == "rain":
#     print("Take your umbrella")
# elif weather == "snow" or weather == "windy":
#     print("Take your Canada Goodse")
# else:
#     print("Enjoy your sunny day")

# temp = int(input("What is temperature today?"))
# if temp >= 30:
#     print("hot")
# elif temp >= 10 and temp <=29:
#     print("picnic time")
# elif temp >= 0 and temp < 10:
#     print("cold")
# else:
#     print("stay home")

# for function
# for waitlist in range(1,6):
#     print("waitlist number {0}" .format(waitlist))

# for cafe_order in ["Jason", "Thomas", "David", "Ola"]:
#     print("{0}, your drink is ready" .format(cafe_order))

# While function
# auction = "Degar's painting"
# index = 3
# while index >= 1:
#     print("{0} is about to be sold. Counting {1}" .format(auction, index))
#     index -= 1
#     if index == 0:
#         print("auction is completed!")


# auction = "Renoir's painting"
# index_1 = 1
# while True:
#     print("{0} is iconic painting. Who wants to participate{1})" .format(auction, index_1))
#     index_1 += 1


# customer = "Monnet"
# person = "unknown"

# while person != customer:
#     print("{0}, your coffee is ready" .format(customer))
#     person = input("What is your name?")


# countine and break
abs = [4, 12]
nbook = [7]
for student in range(1,20):
    if student in abs:
        continue
    elif student in nbook:
        print("You are closing now")
        break
    print("Next line please")


# for fuction in single line

cash = [1, 3, 18, 129, 778 ,9, 92, 38, 50, 1000] #in million dollars
# We want to write all digits
cash = [i*1000000 for i in cash]
print(cash)


name = ["Laurant", "Wayne", "Tom", "Naomi", "Alexander"]
name = [i.upper() for i in name]
print(name)

name = [len(i) for i in name]
print(name)