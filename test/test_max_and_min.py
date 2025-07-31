#pytest --testdox test/test_max_and_min.py 

from src.max_and_min import nc_max, nc_min

def test_max_value_returned(): 
    assert nc_max([1,2,3]) == 3
    assert nc_max([10,200,30]) == 200

def test_min_value_returned(): 
    assert nc_min([1,2,3]) == 1
    assert nc_min([10,200,30]) == 10

def test_no_items_returns_zero(): 
    assert nc_min([]) == 0    
    assert nc_max([]) == 0