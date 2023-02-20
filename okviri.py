xs = input()

l1 = "..#.."
l2 = ".#.#."
l3 = "#." + xs[0] + ".#"

for i in range(1, len(xs)):
    if i % 3 == 2:
        # 5
        l1 = l1 + "..*.."
        l2 = l2 + ".*.*."
        l3 = l3 + "*." + xs[i] + ".*"
    elif i % 3 == 0:
        # 4
        l1 = l1 + ".#.."
        l2 = l2 + "#.#."
        l3 = l3 + "." + xs[i] + ".#"
    elif i % 3 == 1:
        # 3
        l1 = l1 + ".#."
        l2 = l2 + "#.#"
        l3 = l3 + "." + xs[i] + "."
        if i == len(xs) - 1:
            l1 = l1 + "."
            l2 = l2 + "."
            l3 = l3 + "#"     

print(l1)
print(l2)
print(l3)
print(l2)
print(l1)
