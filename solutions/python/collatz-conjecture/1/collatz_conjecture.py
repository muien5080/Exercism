def steps(number):
    s=0
    if number==1:
        return 0
    elif number<1:
        raise ValueError("Only positive integers are allowed")
    else:
        while number!=1:
            if number%2==0:
                number=number/2
                s+=1
            else:
                number=(number*3)+1
                s+=1
    return s