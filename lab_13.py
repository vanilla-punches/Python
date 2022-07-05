# formats
# put empty space and align(right) * You need a space after 0:
print("{0: >10}" .format(500))

# put + in front a number if that number is positive
print("{0: >+10}" .format(500))
# put - in front a number if that number is negative
print("{0: >+10}" .format(-500))

# empty space will be filled with _ and align(left)
print("{0:_<+10}" .format(500))

# put commas every 3 digits
print("{0:,}" .format(10000000000))
print("{0:+,}" .format(10000000000))

print("{0:^<+15,}" .format(10000000))

# decimal
print("{0:f}" .format(7/3))
# if you want specific decimal places, then you put .# in front of f (EX) {0:.3f}
print("{0:.2f}" .format(17/3))