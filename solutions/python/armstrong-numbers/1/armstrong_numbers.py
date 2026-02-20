def is_armstrong_number(number):
    n = str(number)
    p=len(n)
    t=0
    for i in n:
       t += int(i)**p
    return t==number