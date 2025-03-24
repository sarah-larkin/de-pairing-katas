def sum_digits(num):
    if not isinstance(num ,(int)):
        return None
    
    num_str = str(abs(num))
    total = 0
    for digit in num_str:
        total += int(digit)

    return total
    
