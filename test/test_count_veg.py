from src.count_veg import count_veg



def test_type_is_root_return_total_quantity(): 
    #arrange
    test_input_veg = [{"name": 'Parsnip', "type": 'root', "quantity": 4}]
    test_input_type = 'root'
    expected = 4

    #act 
    result = count_veg(test_input_veg, test_input_type)

    assert result == expected

    # assert count_veg([{"name": 'Parsnip', "type": 'root', "quantity": 4}], 'root') == veg['quantity']
   
def test_if_multiple_type_is_root_sum_quantity(): 
    test_input_veg = [{"name": 'Parsnip', "type": 'root', "quantity": 4}, 
                      {"name": 'Carrot', "type": 'root', "quantity": 5}]  
    test_input_type = 'root'
    expected = 9

    result = count_veg(test_input_veg, test_input_type)

    assert result == expected

# def test_if_list_and_type_are_empty_return_zero(): 
#     test_input_veg = []
#     test_input_type = ''
#     expected = 0

#     result = count_veg(test_input_veg, test_input_type)

#     assert result == expected
    
   