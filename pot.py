num = int(input())
sum = 0
for i in range(num):
    x = input()
    b = int(x[-1])
    a = int(x[0:-1])
    sum += a ** b

print(sum)
