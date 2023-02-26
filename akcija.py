n = int(input())
c = []
for i in range(n):
    c.append(int(input()))

c = sorted(c)
price = 0
# print(len(c))
# print("start")
for i in range(-1,-len(c)-1,-3):
    price += sum(c[i:i-2:-1])
print(price)
