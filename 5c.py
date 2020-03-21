def xorR(x,y):
    if x != y:
        return 1
    else:
        return 0
        
x = int(input())
y = int(input())

if x == 1 and y == 0 or x == 0 and y == 1:
    print(xorR(x,y))
else:
    print('use only 0 and 1')


