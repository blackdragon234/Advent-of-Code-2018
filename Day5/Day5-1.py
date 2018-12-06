import os
os.chdir('Day5')

chars = []
resultchars = []

f = open('input.txt')
for polymer in f:
    for c in polymer:
        chars.append(ord(c))
    d = 0
    while d < len(chars) - 1:
        if chars[d] == chars[d+1]+32 or chars[d] == chars[d+1]-32:
            del(chars[d])
            del(chars[d])
            d = d-2
        d += 1
    for c in chars:
        resultchars.append(chr(c))
print(len(resultchars))
