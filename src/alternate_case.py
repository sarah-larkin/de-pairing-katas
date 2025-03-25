def alternate_case(word):
    result = []
    uppercase = True        #first char will be upper 

    for char in word:
        if char.isalpha():      #if letter (not space)
            result.append(char.upper() if uppercase else char.lower())  #if upper is true add upper letter to list, else add lower letter to list
            uppercase = not uppercase       # switch to False 
        else:
            result.append(char)             # ie. for spaces 
    return "".join(result)                  # returning a joined up string (not a list)







#Past attempts

#def alternate_case(word):
  # new_word = ''
    # uppercase = True  
    
    # for char in word:
    #     if char == ' ':
    #         new_word += ' '
    #         uppercase = True  
    #         continue
            
    #     if uppercase:
    #         new_word += char.upper()
    #     else:
    #         new_word += char.lower()
    #     uppercase = not uppercase
    
    # return new_word


# def alternate_case(word):
#     new_word = ''
#     for index, char in enumerate(word):
#         if index % 2 ==0:
#             new_word += char.upper()
#         else:
#             new_word += char.lower()
#         if char != 1:
#             continue
#     return new_word


    # new_word = ''
    # uppercase = True
    # for char in word:
    #     if char == ' ':
    #         new_word += ' '
    #         uppercase = True
    #         continue
    #     new_word += char.upper() if uppercase else char.lower()
    #     uppercase = not uppercase

    # return new_word




    # for char in word:
    #     if word.index(char) == 0 or word.index(char)%2 == 0:
    #         new_word += char.upper()
    #     new_word += char.lower()
    
    # return new_word
    
