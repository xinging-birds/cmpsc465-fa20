# assignment 1 problem 1
# by Justin Huang, Divyesh Johri, Eddie Ubri

list_1 = input().split()
list_2 = input().split()

m = list_1[0]
n = list_2[0]

if m == '0' and n == '0':
    print('0')
elif m == '0':
    print(' '.join(list_2))
elif n == '0':
    print(' '.join(list_1))
else:
    a = list_1[1:]
    b = list_2[1:]
    c = [str(int(m) + int(n))]

    while a or b:
        if not b:
            c.append(a.pop(0))
        elif not a:
            c.append(b.pop(0))
        else:
            if int(a[0]) < int(b[0]):
                c.append(a.pop(0))
            else:
                c.append(b.pop(0))

    print(' '.join(c))
