def get_century(year):
    
    # century = (year // 100) + 1
    # if century % 10 ==  1: 
    #     suffix = "st"
    # if century % 10 == 2: 
    #     suffix = "nd"
    # if century % 10 == 3: 
    #     suffix = "rd"
    # else: 
    #     suffix = "th"
    # return f'{century}{suffix}'


    century = (year - 1) // 100 + 1   

       
    # Determine suffix
    if 11 <= century % 100 <= 13:
        suffix = 'th'
    else:
        last_digit = century % 10
        if last_digit == 1:
            suffix = 'st'
        elif last_digit == 2:
            suffix = 'nd'
        elif last_digit == 3:
            suffix = 'rd'
        else:
            suffix = 'th'
    
    return f"{century}{suffix}"