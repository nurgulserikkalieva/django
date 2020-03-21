n = int(input())
a = []
count = 0

for i in range(n):
    b = int(input())
    a.append(b)

for k in a:
    if k > 0:
        count += 1

print(count)
