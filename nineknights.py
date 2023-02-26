board = []
for i in range(5):
    board.append(list(input()))

# taken = [["_" for i in range(5)] for j in range(5)]
# positions = [(x,y) for x in range(5) for y in range(5)]


def helper(i,j):
    # print("checking: " + str(i) + " " + str(j))
    other_pos = [(i+1, j+2), (i+1, j-2), (i-1, j+2), (i-1, j-2),
                 (i+2, j+1), (i+2, j-1), (i-2, j+1), (i-2, j-1)]
    to_check = [(a,b) for a,b in other_pos if (0 <= a < 5) and (0 <= b < 5)]
    for a,b in to_check:
        if board[a][b] == "k":
            return True
        else:
            pass
    return False

invalid = False
knights = 0

for x in range(5):
    for y in range(5):
        if board[x][y] == "k":
            knights += 1
            if helper(x,y):
                invalid = True
        else:
            pass

if not invalid and knights == 9:
    print("valid")
else:
    print("invalid")

