"""
7 4
#######
#P.GTG#
#..TGG#
#######
"""
"""
8 6
########
#...GTG#
#..PG.G#
#...G#G#
#..TG.G#
########
"""


import sys
lines = []

line = sys.stdin.readline().strip()
while line:
    lines.append(line)
    line = sys.stdin.readline().strip()

x = list(map(int, lines.pop(0).split()))
W = x[0]
H = x[1]

"""
for line in lines:
    print(line)
"""

for i in range(H):
    for j in range(W):
        if lines[i][j] == "P":
            start = (i,j)


def checked_map(lines,checked):
    mp = lines.copy()
    for i,j in checked:
        mp[i] = mp[i][:j] + "0" + mp[i][j + 1:]
    for m in mp:
        print(m)


def possible_moves(x):
    i,j = x
    return [(a,b) for a,b in [(i+1, j), (i-1,j), (i, j+1), (i, j-1)] if (0 < a < H-1) and (0 < b < W-1)]


def can_move(x):
    i,j = x
    if lines[i][j] == "#":
        return False
    elif lines[i][j] == "T":
        print("die")
        raise Exception
        # should not happen
    elif lines[i][j] == "G":
        # print("Gold")
        global score
        score += 1
        return True
    elif lines[i][j] == ".":
        return True
        # will move, score +=1
    elif lines[i][j] == "P":
        return True


def is_draft(lst):
    for i, j in lst:
        if lines[i][j] == "T":
            # print("Draft Detected")
            return True
    return False


def game(pos):
    global checked
    # print("checked: " + str(checked))
    adj_pos = possible_moves(pos)
    checked.append(pos)
    if can_move(pos) and not is_draft(adj_pos):
        for ps in adj_pos:
            if ps not in checked:
                # checked_map(lines,checked)
                # print("move to: " + str(ps))
                game(ps)
            else:
                pass
    else:
        pass


checked = []
score = 0

# print(start)
game(start)
print(score)

"""
for i in range(H):
    for j in range(W):
        if (i,j) in checked:
            lines[i][j] == "0"
"""

