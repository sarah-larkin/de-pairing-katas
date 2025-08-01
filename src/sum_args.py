def sum_args(*args):
    for arg in args: 
        if not isinstance(arg, int): 
            return None
    return sum(args)





#args will be a tuple of all the args
#will get error if try to add floats 
   
     

