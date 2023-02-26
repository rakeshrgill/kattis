n = int(input())
recordings = []
for i in range(n):
    recordings.append(input())

d = set()
while True:
    line = input()
    if line == "what does the fox say?":
        break
    else:
        x = line.split()
        d.add(x[2])

for i in recordings:
    x = i.split()
    output = []
    # print(d)
    for j in x:
        if j not in d:
            # print(j)
            output.append(j)
    print(" ".join(output))
    