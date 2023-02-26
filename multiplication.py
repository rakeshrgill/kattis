'''
6184 9723
7585 387
9448 9653
6540 3390
6950 6440
3239 546
1400 8618
8591 5086
8005 2092
985 3812
8725 6197
7925 2267
3313 9256
1474 2058
1348 7211
3467 9202
7382 2814
3242 7247
417 3666
8576 103
0 0
'''


ls = []
while True:
    line = input().split()
    # x = (int(line[0]),int(line[1]))
    x = (line[0],line[1])
    if x == ('0','0'):
        break
    else:
        ls.append(x)

def helper(n):
    return list(map(int, list(n)))


def mult2(a,b):
    x = a * b
    if x > 9:
        return [x//10,x%10]
    else:
        return [0,x]


def calculate(inner_grid, rows, columns):
    result = []
    numbers = {}
    for i in range(rows):
        for j in range(columns):
            for k in [0,1]:
                # sm is 10^smth power place
                sm = rows + columns - (i+j+k) - 1
                numbers[sm] = numbers.get(sm, []) + [inner_grid[i][j][k]]
    max_key = max(numbers.keys())
    # print(numbers)
    carry = 0
    for i in range(max_key + 1):
        # print("prev res:" + str(result))
        # print("i: " + str(i) + " num: " + str(numbers[i]))
        # print("carry: " + str(carry))
        x = sum(numbers[i]) + carry
        if x >= 10:
            # next carry
            carry = x // 10
        else:
            # next carry
            carry = 0
        result.append(x%10)
    return result
        

for x0, x1 in ls:
    ls_0 = helper(x0)
    ls_1 = helper(x1)
    rows = len(ls_1)
    columns = len(ls_0)
    inner_grid = [[mult2(i,j) for j in ls_0] for i in ls_1]
    result = calculate(inner_grid, rows, columns)
    result.reverse()
    # print(inner_grid)
    # print(result)
    ## printer
    print("+-" + "----" * columns + "-" + "-+")
    x = ""
    for i in ls_0:
        x += "  " + str(i) + " "
    print("| " + x + " " + " |")
    for i in range(rows):
        print("| " + "+---" * columns + "+" + " |")
        middle = "| "
        if i != 0 and not (set(result[i-1::-1]) == {0} or set(result[i-1::-1]) == set()):
            # if it there is nothing above
            top = "|/"
        else:
            top = "| "

        if set(result[i::-1]) == {0}:
            # if it and everything before it is 0
            bottom = "| " 
        else:
            bottom = "|" + str(result[i])

        # columns
        for j in range(columns):
            top += "|" + str(inner_grid[i][j][0]) + " /"
            middle += "| / "
            bottom += "|/ " + str(inner_grid[i][j][1])
        top += "| |"
        middle += "|" + str(ls_1[i]) + "|"
        bottom += "| |"
        print(top)
        print(middle)
        print(bottom)
    print("| " + "+---" * columns + "+" + " |")
    
    x = "|"
    i += 1
    if set(result[i-1::-1]) == {0}:
        x += " "
    else:
        x += "/"

    for j in range(columns-1):
        if set(result[i-1::-1]) == {0}:
            x += " " + " " + "  "
        else:
            x += " " + str(result[i]) + " /"
        i += 1
    x += " " + str(result[i]) + "  "
    x += "  |"
    print(x)
    print("+-" + "----" * columns + "-" + "-+")
