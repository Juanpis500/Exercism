def steps(number):
    total = 0
    while(number > 1):
        if((number % 2) == 0):
            number = number / 2
            total += 1
        else:
            number = number * 3 + 1
            total += 1
    if (number <= 0 ):
        raise ValueError("Only positive integers are allowed")
    
    return total
    
    

