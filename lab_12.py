print("Python", "C++", "R", sep = " vs ") # sep is a separator. Comma will be replaced by a separator.

print("Python", "C++", "R", sep = " vs ", end = " ") # end will bring the next "print" to the end of current "print"
print("Which language is more powerful?")

print("Python", "C++", "R", sep = " vs ", end = "? ") # end will add "?" at the end of current "print"
print("Which language is more powerful?")


import sys
print("Python", "Java", file = sys.stdout)
print("Python", "Java", file = sys.stderr) # Only print out error msg?


scores = {"Statistics":100, "Python": 98, "Finance": 90}
for subject, score in scores.items(): # scores.items() sends subject to key and score to value that was defined in scores
    #print(subject, score)
    print(subject.ljust(10), str(score).rjust(3), sep = " : ") # organizing lines and spaces


# Filling 0s in numbers
for numb in range(1,16):
    print("Waiting number:" + str(numb).zfill(3))

answer = input("Enter your input:")
print("The input you just entered is " + answer) # Default setting is string. When you input an integer, output will be a string