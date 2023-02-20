cont = True
xs = []

while cont:
    x, y, z = tuple(input().split())
    if x == y == z == "0":
        cont = False
    else:
        xs.append((int(x), int(y), int(z)))

for x, y, z in xs:
    if ((x**2 + y**2) == (z**2)) or ((y**2 + z**2) == (x**2)) or ((x**2 + z**2) == (y**2)):
        print("right")
    else:
        print("wrong")
