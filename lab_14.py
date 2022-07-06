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

# score_file = open("score.txt", "r")
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")
# score_file.close()


# pickle ---> save data as a file, so people save data in a file and others can use file to import data and use it

import pickle
profile_file = open("profile.pickle", "wb") # "wb" is for saving data in a file
profile = {"Name": "Ian", "Age": 33, "Interests": ["Statistics", "Finance", "Soccer"]}
print(profile)
pickle.dump(profile, profile_file)
profile_file.close()

# profile_file = open("profile.pickle", "rb") # "rb" is to use file to import data
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()


# with

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))


with open("study.txt", "w") as study_file:
    study_file.write("University of Toronto, Mathematical Finance")

with open("study.txt", "r") as study_file:
    print(study_file.read())