reps = int(input())
printout = []


def SSD(b, n):
    counter = 1
    while (b**counter) <= n:
        counter += 1
    counter -= 1
    ls = []
    for i in range(counter, -1, -1):
        y = n // b ** i
        ls.append(y)
        n = n - (y * b**i)
    return ls


for i in range(reps):
    x = input().split()
    k = int(x[0])
    b = int(x[1])
    n = int(x[2])
    finalsum = 0
    for j in SSD(b, n):
        finalsum += j ** 2
    printout.append(str(x[0] + " " + str(finalsum)))


for i in printout:
    print(i)
