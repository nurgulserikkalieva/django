n = int(input())
a = []
count = 0
for i in range(n):
    b = int(input())
    a.append(b)

for k in range(len(a)):
    if a[k-1] < a[k]:
        count += 1

print(count)
