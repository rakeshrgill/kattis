import sys
d = set()
lines = []

line = sys.stdin.readline().strip()
while line:
    new_line = []
    s = line.strip().split()
    for word in s:
        if word.lower() not in d:
            new_line.append(word)
            d.add(word.lower())
        else:
            new_line.append(".")
    lines.append(" ".join(new_line))
    line = sys.stdin.readline().strip()



for i in lines:
    print(i)