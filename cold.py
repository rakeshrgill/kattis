n = int(input())
temp = input()
x = list(map(int,temp.split(' ')))
count = 0
for i in x:
    if i < 0:
        count +=1
print(count)
    
