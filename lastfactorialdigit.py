num = int(input())


def factorial_last(x):
    current = 1
    for i in range(1, x + 1):
        current = (current * i) % 10
    return current


x = []
for i in range(num):
    x.append(factorial_last(int(input())))

for i in x:
    print(i)
