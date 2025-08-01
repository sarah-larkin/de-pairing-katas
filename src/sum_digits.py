# def sum_digits(num):
#     if not isinstance(num ,(int)):
#         return None
    
#     num_str = str(abs(num))
#     total = 0
#     for digit in num_str:
#         total += int(digit)

#     return total

#----------------------------------------
    
# def sum_args(num):
#     if isinstance(num, (int, float)): 
#         str_num = str(num).replace(".", "")
#         num_lst = [int(digit) for digit in str_num]
#         return sum(num_lst)
#     return "error"


#isdigit() 

def sum_digits(num):
    if not isinstance(num, (int, float)): 
        return "error"
    num_lst = [int(digit) for digit in str(num) if digit.isdigit()]
    return sum(num_lst)
