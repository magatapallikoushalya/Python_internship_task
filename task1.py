mixed_list = [10, "Python", 3.14, 25, "Code", 7.8, "Internship"]
integers = []
strings = []
floats = []
for item in mixed_list:
    if type(item) == int:
        integers.append(item)
    elif type(item) == str:
        strings.append(item)
    elif type(item) == float:
        floats.append(item)
print("Integers:", integers)
print("Strings:", strings)
print("Floats:", floats)
