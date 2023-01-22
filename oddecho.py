n = int(input())

words =[]

for i in range(0,n):
    user_input = input()
    words.append(user_input)

for x in  range(0,n,2):
    print(words[x])
