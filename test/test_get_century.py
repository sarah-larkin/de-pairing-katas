from src.get_century import get_century

def test_return_correct_suffix_th(): 
    input_year = 1892
    expected = '19th'

    result = get_century(input_year)

    assert result == expected 

def test_if_year_less_than_four_digits(): 
    input_year = 189
    expected = '2nd'

    result = get_century(input_year)

    assert result == expected 

def test_return_correct_suffix(): 
    assert get_century(212) == "3rd"
    assert get_century(56) == "1st"
    assert get_century(2166) == "22nd"
    assert get_century(2466) == "25th"

def test_turn_of_century_years(): 
    assert get_century(1999) == "20th"
    assert get_century(2000) == "20th"
    assert get_century(2001) == "21st"

def test_years_below_20(): 
    assert get_century(1001) == "11th"
    assert get_century(1111) == "12th"
    assert get_century(1222) == "13th"

def test_invalid_year(): 
    assert get_century(0) == "Invalid year"
    assert get_century(21546231) == "Invalid year"

