n = int(input())
a = []

for i in range(n):
    b = int(input())
    a.append(b)

for k in range(len(a)):
    if a[k] % 2 == 0:
        print(k)
