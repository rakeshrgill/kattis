x = input().split()
day = int(x[0])
month = int(x[1])
# Jan 1 is a Friday
monthd = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
daycount = day - 4
for i in range(1, month):
    daycount += monthd[i]
dayofweek = daycount % 7
dayd = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 0: "Sunday"}
print(dayd[dayofweek])
