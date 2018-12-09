n = 6
s = n
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            print(' ', end='')
        elif i == 0 and j == n-1:
            print('*', end='')
        elif j == 0 and i == n - 1:
            print(' ', end='')
        elif j == n - 1 and i == n - 1:
            print('*', end='')
        elif i == 0 or i == n-1:
            print('*', end=' ')
        elif j == 0 or j == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
for i in range(2):
    for j in range(8+i):
        if j == 7+i:
            print('*', end='')
        else:
            print(' ', end='')
    print()



