# # glob : a function to search files
# import glob
# from selectors import EpollSelector
# print(glob.glob("*.py")) # show all files that are .py

# os : provide basic operations
# import os
# print(os.getcwd()) # shwo your current directory

# folder = "simple_dir"

# if os.path.exists(folder):
#     print("Already existing")
#     os.rmdir(folder)
#     print(folder, "folder is removed")
# else:
#     os.makedirs(folder) # creating a folder
#     print(folder, "folder is created")

# print(os.listdir())

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("Today is", datetime.date.today())

# Counting dates
today = datetime.date.today()
td = datetime.timedelta(days = 365)
print("Out 1st year anniversary is", today + td)