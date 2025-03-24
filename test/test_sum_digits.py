from src.sum_digits import sum_digits

# Tests for sum_digits

# TEST 1 - sum_digits returns the input number when passed a single digit number
# This test has two ASSERTIONS being made
# The same behaviour is being tested but with different inputs - 1 and 9

# E.g. sum_digits(1) should output 1
# E.g. sum_digits(9) should output 9


# Once you have got the first test passing, then you can write your next one.
# If you've already handled a single digit, your next test could test for multi-digit inputs.

# E.g. sum_digits(99) should output 18
# E.g. sum_digits(123) should output 6

# HINT: Remember to see the test *fail* first, then write the code to pass the test

# Why this test?
# A multi-digit input means you now have to implement to 'addition' part of this function,
# but you don't have to think about the logic for dealing with/ignoring non-digit characters yet
# (that's for our next test!)


# Once you have successfully passed the above test, then you can write your next test.
# A good next test might be to check that your function handles non-numerical characters correctly (i.e. ignores them)

# E.g. sum_digits(10.5) should output 6
def test_single_digit_number():
    assert sum_digits(1) == 1
    assert sum_digits(9) == 9
    

def test_multi_digit_number():
    assert sum_digits(11) == 2
    assert sum_digits(123) == 6

def test_not_negative_number():
    assert sum_digits(-1) == 1
    assert sum_digits(-55) == 10

def test_only_if_number():
    assert sum_digits('a') == None
    assert sum_digits('1!') == None






