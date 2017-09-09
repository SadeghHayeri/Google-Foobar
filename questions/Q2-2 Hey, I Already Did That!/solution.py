def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

def getNext(n, b, k):
    x = ''.join(sorted(list(n), reverse=True))
    y = ''.join(sorted(list(n)))
    z = baseN(int(x, b) - int(y, b), b)
    return '0' * (k - len(z)) + z

def answer(n, b):
    k = len(n)
    index = 0
    funded = {}

    while True:
        if n in funded:
            return index - funded[n]
        else:
            funded[n] = index
            index += 1

        n = getNext(n, b, k)


# answer('210022', 3)   #-> 3
