import random
# min_value = int(input("min"))
# max_value = int(input("max"))
# count = int(input("count"))
min_value = 3
max_value = 13
count = 10
valdict = {}

for x in range(count):
    val =random.randrange(min_value, max_value)
    if val not in valdict:
        valdict[val] = [[], 0]
    valdict[val][0].append(x)
    valdict[val][1] += 1
    # print(val)
# print()

keys = valdict.keys()

lkeys = list(keys)
# print(lkeys)
# # Open the file in write mode (or append mode if you want to add to an existing file)
with open('data.txt', 'w') as file:
    # Join the list elements into a single string separated by newlines
    for r in valdict.keys():
        file.write(f"{str(r)} ")
print(f"{len(keys)}")
print(min(lkeys))
print()