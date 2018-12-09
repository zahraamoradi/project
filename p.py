n = 1
s = n+2
for i in range(n+2):
    if i == 1:
        print('* *')
    for j in range(n+2):
        if j == 0:
            print('*', end='')
    for p in range(2*i+1):
        print(' ', end='')
    for k in range(i):
        if k == i-1:
            print('*', end='')

    if i == n+1:
        print()
        for j in range(n+2):
            if j == 0:
                print('*', end='')
        for p in range(2 * i+1):
            print(' ', end='')

        for k in range(i):
            if k == i - 1:
                print(' *', end='')
        print()

        for j in range(n+2):
            if j == 0:
                print('*', end='')
        for p in range(2 * i+1):
            print(' ', end='')
        for k in range(i):
            if k == i - 1:
                print('  *', end='')
    print()

for i in range(n+2):

    if i == 1:
        for j in range(s):
            if j == 0:
                print('*', end='')
        for p in range(2 * s+1):
            print(' ', end='')
        for k in range(s):
            if k == s - 1:
                print(' *', end='')
        print()

    for j in range(s):
        if j == 0:
            print('*', end='')
    for p in range(2*s+1):
        print(' ', end='')
    for k in range(s):
        if k == s-1:
            print('*', end='')

    if i == n+1:
        print()
        print('* *', end='')
    s = s-1
    print()
print('*')
s = n
for i in range(4):
    print('*')


