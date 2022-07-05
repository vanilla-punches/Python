from email.errors import MalformedHeaderDefect


def std_weight(gender, height):
    if gender == "M":
        return height * height * 22
    else:
        return height * height * 21

height = 175 #cm
gender = "M"

weight = round(std_weight(gender, height / 100), 2)
print("Ideal weight for {0} with {1}cm is {2}" .format(gender, height, weight))