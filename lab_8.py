from math import *
from random import *

cnt = 0

for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[O] {0} customer was served for {1} minutes" .format(i, time))
        cnt += 1
    else:
        print("[X] {0} customer was not served because it tooke {1} minutes" .format(i, time))

print("totoal number of customer: {0}" .format(cnt))