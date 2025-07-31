#take a list of numbers 
#return True is ascending 
#return False if not ascending 
#also return False list is empty


# def are_ordered(nums):
#     if not nums: 
#         return False
#     if nums == sorted(nums): 
#         return True
#     else:
#         return False



def are_ordered(nums):
    if not nums: 
        return False 
    return nums == sorted(nums)