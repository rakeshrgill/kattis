x = input()
y = ""
for i in range(len(x) - 1):
    if x[i] == x[i + 1]:
        pass
    else:
        y += x[i]
print(y + x[-1])
