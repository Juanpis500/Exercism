def is_armstrong_number(number):
    txt = str(number)
    total = 0
    for num in txt:
        total += int(num) ** len(txt)

    if(total == number): 
        return True 
    else: 
        return False
