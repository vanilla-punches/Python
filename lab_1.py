# Lab1

station = "Bay"
print(station, "station is between Bloor-Yonge and St.George stations")

#Simple Calculations
print(1+5) #6
print(4*2) #8
print(7/2) #3.5

print(2**3) #2^3 = 8
print(5%2) #remainder
print(25//3) #quotient
print (8 ==8) #8 = 8
print (10 >= 20)
print (10>3>9)

number = 3*2*5
number = number +10
print(number)

print(number /10)
print(number +30)

number -= 50
number *= 2
print(number)



print(abs(-19)) #19
print(pow(5,2)) #5^2
print(max(10,20,30,40,50))
print(round(3.92)) #4

from math import *
print(floor(5.82))
print(ceil(31.51))
print(sqrt(9))

from random import *
print(random()) #random number between 0.0 and 1.0
print(random() * 10)
print(int(random() * 10))
print(int(random() * 10) + 1) #random number between 1 and 10

print(randrange(1,50)) #random number range between 1 and 49
print(randint(1,49)) #random number between 1 and 49


study = randint(4,28)
print("We are going to study on", study, "of every month")