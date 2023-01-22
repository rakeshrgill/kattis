x = input()
pos = 1
for i in x:
    if i == "A":
        if pos == 1:
            pos = 2
        elif pos == 2:
            pos = 1
        elif pos == 3:
            pass
    elif i == "B":
        if pos == 1:
            pass
        elif pos == 2:
            pos = 3
        elif pos == 3:
            pos = 2
    elif i == "C":
        if pos == 1:
            pos = 3
        elif pos == 2:
            pass
        elif pos == 3:
            pos = 1
print(pos)
