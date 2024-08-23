x = 5
for i in range(5):
    for j in range(5):
        if i+j==x-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()