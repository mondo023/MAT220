largest = []
for i in range(0,70):
    found = False
    for x in range(0, 12):
        for y in range(0, 9):
            for z in range(0, 4):
                if (6*x + 9 * y + 20 * z == i):
                    found = True
    if not found:
        largest.append(i)
print(largest[-1])
