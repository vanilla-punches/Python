# sample
from random import *

# comments = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
comments = range(1,21)
comments = list(comments)
print(type(comments))
print(comments)

shuffle(comments)
print(comments)

winners = sample(comments, 4)
print("----- Announcemnet -----")
print("1st Winner: {0}" .format(winners[0]))
print("2nd and 3rd Winners: {0}" .format(winners[1:]))