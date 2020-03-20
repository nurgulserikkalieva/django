n = int(input())
i = 1
c = 0

while i < n:
    i += 1
    if n % i == 0:
        c = i
        break

print(c)
