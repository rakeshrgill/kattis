x = input().split()
if x[0] == "E":
    y = ""
    i = 0
    while i < len(x[1]):
        j = 1
        while (i + j < len(x[1])) and (x[1][i] == x[1][i + j]):
            j = j + 1
        y = y + x[1][i] + str(j)
        i = i + j
    print(y)
else:
    y = ""
    for i in range(0, len(x[1]), 2):
        y = y + (x[1][i] * int(x[1][i + 1]))
    print(y)
