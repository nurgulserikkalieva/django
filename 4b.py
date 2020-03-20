n = int(input())
b = []

for i in range(n):
    a = int(input())
    b.append(a)

for k in b:
    if k % 2 == 0:
        print(k)
