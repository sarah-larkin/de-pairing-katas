from src.are_ordered import are_ordered

def test_empty_list(): 
    assert are_ordered([]) == False 

def test_asc_list(): 
    assert are_ordered([1,2,3]) == True
    assert are_ordered([4,5,6]) == True 
    assert are_ordered([10,11,12]) == True 
    assert are_ordered([22,28,33,45,66]) == True  

def test_desc_list(): 
    assert are_ordered([3,2,1]) == False  
    assert are_ordered([10,9,8]) == False
    assert are_ordered([99,88,77])== False


