f = str(input("What Phrase do you want to Encrypt?(No caps/ints Pls) "))

r = str(input("What Number do you want to Set the Reel to? "))

pC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
      'x', 'y', 'z', 'Ω', ' ', '∆', '?', '!', '£', 'ß', 'œ', 'π', '«', 'ø', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I',
      'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '\'']


r1 = int(r[0:2])

def encript(r, f):

    eF = ""

    for i in f:

        iD = pC.index(i)

        iN = iD + r

        if iN >= 64:
            iN = iN % 64

        eF = eF + pC[iN]

        r += 1

        if r > 64:
            r = 1

    return(eF)


a = 2
b = 4

f1 = [encript(r1, f)]

for i in range(1, 11):

    ii = i-1

    rx = int(r[a:b])

    x = encript(rx, f1[ii])

    f1.append(x)

    a += 2
    b += 2

    if i == 10:
        print(f1[i])
