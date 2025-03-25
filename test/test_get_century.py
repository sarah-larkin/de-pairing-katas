from src.get_century import get_century


#TODO: correct suffix th or st or rd or nd 
#TODO: 11th, 12th, 13th 
#TODO: not year <1 or >9999 


# def test_return_correct_century():
#     input_year = 1999
#     expected = '20'

#     result = get_century(input_year)

#     assert result == expected 

def test_return_correct_suffix(): 
    input_year = 1892
    expected = '19th'

    result = get_century(input_year)

    assert result == expected 

def test_if_year_less_than_four_digits(): 
    input_year = 189
    expected = '2nd'

    result = get_century(input_year)

    assert result == expected 