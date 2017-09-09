def answer(string):
    ans = 0
    rightCount = 0
    for c in string:
        if c == '>':
            rightCount += 1
        elif c == '<':
            ans += 2 * rightCount
    return ans


# answer('>----<')  #-> 2
# answer('<<>><')   #-> 4
