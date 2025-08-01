from src.sum_ascii import sum_ascii

def test_returns_str(): 
    assert type(sum_ascii(["Adam"])) == str

def test_returns_name_when_one_name_passed(): 
    assert sum_ascii(["Adam"]) == "Adam"

def test_returns_name_with_highest_score_when_two_names_passed(): 
    assert sum_ascii(["Sarah", "Mary"]) == "Sarah"