from src.check_usernames import check_usernames

#@pytest.mark.it("returns false for empty list")
def test_empty_list_returns_false(): 
    assert check_usernames([]) == False

def test_returns_true_if_5_letters_or_more(): 
    assert check_usernames(["12345"]) == True 
    assert check_usernames(["1234"]) == False

def test_lower_case_only(): 
    assert check_usernames(["ABCDE"]) == False 
    assert check_usernames(["aAvVcC"]) == False
    assert check_usernames(["abcde"]) == True

def test_permitted_punctuation_only():
    assert check_usernames(["a!b$c&d*"]) == False 
    assert check_usernames(["a_b_c_d"]) == True
    assert check_usernames([",./?#\~"]) == False 

def test_less_than_20_characters(): 
    assert check_usernames(["abcdefghijklmnopqrst"]) == True
    assert check_usernames(["abcdefghijklmnopqrstuv"]) == False
    assert check_usernames(["abcdefghijklmnopqrstuvwxyz"]) == False