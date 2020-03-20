n = int(input())
v = 1
b = False

while v < n:
    v *= 2
    if v == n:
        b=True

if b == True:
    print("YES")
else:
    print("NO") 
