"""
takes a list of usernames 
returns True if all valid
returns False if not valid 

username: 
- at least 5 characters long 
- only lowercase letters, numbers, underscores
- no longer than 20 characters 

"""

import string 

# def check_usernames(usernames):
#     permitted = string.ascii_lowercase + string.digits + "_"
#     if not usernames: 
#         return False
#     for username in usernames: 
#         if len(username) < 5 or len(username) > 20: 
#             return False
#         for letter in username: 
#             if letter not in permitted: 
#                 return False
#     return True

def check_usernames(usernames):
    permitted = string.ascii_lowercase + string.digits + "_"
    if not usernames: 
        return False
    for username in usernames: 
        if len(username) < 5 or len(username) > 20: 
            return False
        if not all(letter in permitted for letter in username):  #==> user all() for remove nested for loop
            return False
    return True

#all() --> Return True if all elements of the iterable are true (or if the iterable is empty).