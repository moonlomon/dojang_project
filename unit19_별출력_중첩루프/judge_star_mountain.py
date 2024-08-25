# 풀이1
x = int(input())
for i in range(x):
    for j in range(2*x-1):
        if i+j<x-1 or j-i>=x:
            print(" ", end='')
        else:
            print('*', end='')
    print()

# 풀이2
x = int(input())
for i in range(1,x+1):
    print(' '*(x-i)+'*'*(2*i-1))