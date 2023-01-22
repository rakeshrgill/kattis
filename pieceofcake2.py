a = input().split()
n = int(a[0])
h = int(a[1])
h_ = n - h
v = int(a[2])
v_ = n - v
print(max([h * v, h_ * v, h * v_, h_ * v_]) * 4)
