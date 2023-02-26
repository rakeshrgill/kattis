a = list(map(int,input().split()))
w = int(input())
# from itertools import permutations
ones = a[0]
twos = a[1]
threes = a[2]
# books = [i+1 for i in range(len(a)) for j in range(a[i])]
# books.sort(reverse=True)
# bookcase = [0]
'''
for bookwidth in books:
    shelf = 0
    while True:
        if bookcase[shelf] + bookwidth <= w:
            bookcase[shelf] += bookwidth
            break
        else:
            # if can't be added check the next  shelf
            shelf += 1
            # if shelf does not exist
            if shelf >= len(bookcase):
                bookcase = bookcase + [0]
        # print("bookcase: " + str(bookcase))
# print("bookcase: " + str(bookcase))
'''
shelves = 0
remainingwidth = w
while (ones > 0) or (twos > 0) or (threes > 0):
    remainingwidth = w
    lastplaced = 0
    while remainingwidth >= 3 and threes > 0:
        remainingwidth -= 3
        threes -= 1
        lastplaced = 3
    while remainingwidth >= 2 and twos > 0:
        remainingwidth -= 2
        twos -= 1
        lastplaced = 2
    while remainingwidth >= 1 and ones > 0:
        remainingwidth -= 1
        ones -= 1
        lastplaced = 1
    if remainingwidth == 1 and lastplaced == 3 and twos >= 2:
        remainingwidth -= 1;
        threes += 1;
        twos -= 2;
        lastPlaced = 2;
    shelves += 1

'''
#include <iostream>

int main()
{
    int ones, twos, threes, shelfWidth;
    std::cin >> ones >> twos >> threes >> shelfWidth;

    int shelvesNeeded{0};

    while (ones > 0 || twos > 0 || threes > 0)
    {
        int lastPlaced{0};
        int currentShelfWidthRemaining{shelfWidth};

        while (currentShelfWidthRemaining >= 3 && threes > 0) // Pack 3s until unable
        {
            currentShelfWidthRemaining -= 3;
            threes -= 1;
            lastPlaced = 3;
        }
        while (currentShelfWidthRemaining >= 2 && twos > 0) // Pack 2s until unable
        {
            currentShelfWidthRemaining -= 2;
            twos -= 1;
            lastPlaced = 2;
        }
        while (currentShelfWidthRemaining >= 1 && ones > 0) // Pack 1s until unable
        {
            currentShelfWidthRemaining -= 1;
            ones -= 1;
            lastPlaced = 1;
        }
        if (currentShelfWidthRemaining == 1 && lastPlaced == 3 && twos >= 2)
        {
            currentShelfWidthRemaining -= 1;  // Not strictly necessary
            threes += 1;
            twos -= 2;
            lastPlaced = 2;  // Not strictly necessary
        }

        shelvesNeeded += 1;
    }

    std::cout << shelvesNeeded << '\n';
}
'''


'''
while books:
    bookwidth = books.pop(0)
    shelf = 0
    while True:
        if (bookwidth == 2) and (w-bookcase[shelf]) == 1 and bookcase[shelf] >= 3 and books[0] == 2:
            bookwidth2 = books.pop(0)
            bookcase[shelf] -= 3
            books.insert(0, 3)
            bookcase[shelf] += bookwidth
            bookcase[shelf] += bookwidth2
            break
        elif bookcase[shelf] + bookwidth <= w:
            bookcase[shelf] += bookwidth
            break
        else:
            # if can't be added check the next  shelf
            shelf += 1
            # if shelf does not exist
            if shelf >= len(bookcase):
                bookcase = bookcase + [0]
        # print("bookcase: " + str(bookcase))
# print("bookcase: " + str(bookcase))

'''
print(shelves)
