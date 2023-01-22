x = int(input())


def numberof(n):
    if n == 1:
        return 3
    else:
        return numberof(n - 1) * 2 - 1


print(numberof(x)**2)
