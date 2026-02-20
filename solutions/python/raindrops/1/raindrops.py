def convert(number):
    r=""
    if number%3 == 0:
        r=r+"Pling"
    if number%5 == 0:
        r=r+"Plang"
    if number%7 == 0:
        r+="Plong"
    if r=="":
        return str(number)
    else:
        return r
