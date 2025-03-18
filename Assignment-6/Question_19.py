# 19. From a list containing ints, strings and floats, make three lists to store them separately

lst = [1, 2, 3, "a", "b", "c", 4.0, 5.0, 6.0]
ints = []
strings = []
floats = []

for i in lst:
    if type(i) == int:
        ints.append(i)
    elif type(i) == str:
        strings.append(i)
    elif type(i) == float:
        floats.append(i)

print(f"List: {lst}")
print(f"Ints: {ints}")
print(f"Strings: {strings}")
print(f"Floats: {floats}")