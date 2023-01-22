x = int(input())

while not ((x >= 1) and (x <= 9)):
    x = str(x).replace("0", "")
    mult = 1
    for i in x:
        mult *= int(i)
    x = mult

print(x)
