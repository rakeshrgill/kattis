n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
for i in range(n-1,-1,-1):
    print(numbers[i])
