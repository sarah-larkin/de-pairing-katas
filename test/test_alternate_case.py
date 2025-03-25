from src.alternate_case import alternate_case

def test_single_upper_character():
    test_input = 'A'
    expected = 'A'
    result = alternate_case(test_input)
    assert result == expected

def test_single_lower_character_returns_upper():
    test_input = 'a'
    expected = 'A'
    result = alternate_case(test_input)
    assert result == expected

def test_two_character_return_first_upper_second_lower():
    test_input = 'aa'
    expected = 'Aa'
    result = alternate_case(test_input)
    assert result == expected

def test_three_character_return_alternate():
    test_input = 'aaa'
    expected = 'AaA'
    result = alternate_case(test_input)
    assert result == expected

def test_multiple_lower_character_word_return_alternate():
    test_input = 'hello'
    expected = 'HeLlO'
    result = alternate_case(test_input)
    assert result == expected

def test_multiple_lower_word_return_alternate():
    test_input = 'hello world'
    expected = 'HeLlO wOrLd'
    result = alternate_case(test_input)
    assert result == expected


    



# A --> A 
# a --> A 
# aA --> AA 