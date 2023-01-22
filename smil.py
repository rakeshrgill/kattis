x = input()
substrings = [":)",";)", ":-)",";-)"]

def check(tocheck, substr):
    start = 0
    templist = []
    while True:
        n = tocheck.find(substr, start)
        if n == -1:
            return templist
        else:
            templist.append(n)
            start = n+1
            
        
final = []
for substring in substrings:
    final.extend(check(x,substring))

for i in final:
    print(i)
