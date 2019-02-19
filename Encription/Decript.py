
nC = str(input("Enter encrypted string: "))

r = str(input("What Number did you Set the Reel to? "))

pC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
      'x', 'y', 'z', 'Ω', ' ', '∆', '?', '!', '£', 'ß', 'œ', 'π', '«', 'ø', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I',
      'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '\'']


r1 = int(r[0:2])

def decypt(r, f):

    of = ""

    for i in f:

        id = pC.index(i)

        inn = id - r

        if inn < 0:
            inn += 64

        of = of + pC[inn]

        r += 1

        if r > 64:
            r = 1

    return of

a = 2
b = 4

f1 = [decypt(r1, nC)]

for i in range(1, 11):

    ii = i-1

    rx = int(r[a:b])

    x = decypt(rx, f1[ii])

    f1.append(x)

    a += 2
    b += 2

    if i == 10:
        print(f1[i])
