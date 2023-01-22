reps = int(input())

ans = []

for i in range(reps):
    x = input()
    if x[:11] == "Simon says " and x[11:] > "":
        ans.append(x[11:])

for j in ans:
    print(j)
