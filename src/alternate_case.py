def alternate_case(word):
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





    new_word = ''
    for index, char in enumerate(word):
        if index % 2 ==0:
            new_word += char.upper()
        else:
            new_word += char.lower()
        if char != 1:
            
            continue
    return new_word


    # for char in word:
    #     if word.index(char) == 0 or word.index(char)%2 == 0:
    #         new_word += char.upper()
    #     new_word += char.lower()
    
    # return new_word
    
