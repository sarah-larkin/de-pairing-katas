def sum_ascii(names):
    """
    take a list of names 
    calculate each names score based on each character's ascii value 
    return the name with the highest score 
    """
    #returns highest score only: 
    # name_scores = []
    # score = 0 
    # for name in names: 
    #     name = name.lower() 
    #     for letter in name: 
    #         score += ord(letter)
    #     name_scores.append(score)
    # return max(name_scores)


#convert to dict, name being the keys
#calculate the ascii value and make the value for each key 
#return the key with the highest value 

    name_dict = dict.fromkeys(names, 0)
    
    for name in names: 
        score = 0 
        for letter in name: 
            score += ord(letter.lower())
        name_dict[name] = score
    return max(name_dict, key=name_dict.get)
    

#getting max from the values in a dict: 
#result = max(dict, key=dict.get)



