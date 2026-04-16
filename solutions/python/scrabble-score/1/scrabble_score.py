def score(word):
    vone = {'A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'}
    vtwo = {'D','G'}
    vthree = {'B', 'C', 'M', 'P'}
    vfour = {'F', 'H', 'V', 'W', 'Y'}
    vfive = {'K'}
    veight = {'J', 'X'}
    vten = {'Q','Z'}
    v = 0
    word = word.upper()
    for ch in word:
        if ch in vone:
            v+=1
        elif ch in vtwo:
            v+=2
        elif ch in vthree:
            v+=3
        elif ch in vfour:
            v+=4
        elif ch in vfive:
            v+=5
        elif ch in veight:
            v+=8
        else:
            v+=10
    return v