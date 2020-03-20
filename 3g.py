x = int(input())
n = 0

for i in range(2,x+1):
    if x % i == 0:
        n = i
        break

print(n)
        
        
        
