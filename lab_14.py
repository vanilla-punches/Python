# score_file = open("score.txt", "w") # "w" is to write
# print("Stats : 100", file=score_file)
# print("Python : 90", file=score_file)
# print("Finance : 95", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a") # "a" is to write on the existing file
# score_file.write("Machine learning : 90")
# score_file.write("\nStochastics : 95") # "when you use score_file.write, there is no line change. Thus, you need to put \n"
# score_file.close()

# score_file = open("score.txt", "r") # "r" is to read a file ---> read everything
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r")
# print(score_file.readline(), end=("")) # read line by line
# print(score_file.readline(), end=(""))
# print(score_file.readline(), end=(""))
# print(score_file.readline(), end=(""))
# score_file.close()

# score_file = open("score.txt", "r")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

score_file = open("score.txt", "r")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()