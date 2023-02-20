x = []
for i in range(3):
    temp = input().split()
    a = int(temp[0])
    b = int(temp[1])
    x.append((a, b))

i = x[0]
j = x[1]
k = x[2]

# print(x)

def line_length(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x1 - x2)**2 + (y1 - y2)**2)**(1 / 2)


def d_calc(c_, c, m):
    x1, y1 = c_
    d = (x1 + (y1 - c)*m)/(1 + m**2)
    return d


def cm_calc(a_, b_):
    x1, y1 = a_
    x2, y2 = b_
    m = (y2-y1)/(x2-x1)
    c = (x2*y1-x1*y2)/(x2-x1)
    return c, m


def mathy(a_, b_, c_):
    x1, y1 = c_
    c, m = cm_calc(a_, b_)
    d = d_calc(c_, c, m)
    # print("d  " + str(d))
    x4 = round(2 * d - x1)
    y4 = round(2 * d * m - y1 + 2 * c)
    print(str(x4) + " " + str(y4))


if line_length(i, j) == line_length(i, k):
    # jk is long
    mathy(j, k, i)

elif line_length(i, j) == line_length(j, k):
    #  ik is  long
    mathy(i, k, j)

elif line_length(j, k) == line_length(i, k):
    # ij is long
    mathy(i, j, k)
