def points(card):
    if card[0] == "A":
        return 11
    elif card[0] == "K":
        return 4
    elif card[0] == "Q":
        return 3
    elif card[0] == "T":
        return 10
    elif card[0] == "8" or card[0] == "7":
        return 0
    elif card[1] == B:
        if card[0] == "J":
            return 20
        elif card[0] == "9":
            return 14
    else:
        if card[0] == "J":
            return 2
        elif card[0] == "9":
            return 0


x = input().split()
B = x[1]
sum = 0
for i in range(4 * int(x[0])):
    card = input()
    sum += points(card)
print(sum)
