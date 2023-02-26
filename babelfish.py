import sys
d = {}
words = []
read = True
write = False

line = sys.stdin.readline().strip()
while line:
    s = line.strip().split()
    d[s[1]] = s[0]
    line = sys.stdin.readline().strip()


line = sys.stdin.readline().strip()
while line:
    words.append(d.get(line.strip(), "eh"))
    line = sys.stdin.readline().strip()

for i in words:
    print(i)