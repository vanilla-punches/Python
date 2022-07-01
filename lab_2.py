sentence = 'I am a boy'
print(sentence)
sentence2 = "You are a girl"
print(sentence2)
sentence3 = """
I am a boy,
and you are a girl
"""
print(sentence3)


#Slicing
SIN = "512-597-401"
BDAY = "20121222"
print("province: ", SIN[0])
print("mid numbers: ", SIN[4:7]) #Range betwen 4 and 6
print("year: ", BDAY[0:4])
print("year: ", BDAY[:4])
print("year: ", BDAY[-8:-4]) #We can count from back. Then the last number is starting from -1
print("month: ", BDAY[4:6])
print("day: ", BDAY[6:8])


word = "Python is cool"
print(word.lower())
print(word.upper())
print(word[0].isupper()) #isupper is chekcin if it is a upper letter or not
print(len(word))
print(word.replace("Python", "C++"))

index = word.index("o")
print(index)
index = word.index("o", index + 1)
print(index)
print(word.find("o"))

print(word.count("o"))