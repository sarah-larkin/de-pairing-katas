from src.sum_args import sum_args

def test_returns_arg_when_passed_one_arg(): 
    assert sum_args(1) == 1
    assert sum_args(22) == 22

def test_returns_sum_of_args_when_passed_multiple_args(): 
    assert sum_args(1,2,3) == 6
    assert sum_args(22,33) == 55

def test_returns_0_when_no_args_passed(): 
    assert sum_args() == 0 

def test_returns_None_if_passed_incorrect_type(): 
    assert sum_args("one", "two") == None 
    assert sum_args(1.2,1.2,1.2) == None

