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

def test_with_different_veg_types():
    test_input_veg = [{"name": 'Parsnip', "type": 'root', "quantity": 4},
  {"name": 'Broccoli', "type": 'brassica', "quantity": 1},
  {"name": 'Carrot', "type": 'root', "quantity": 5},
  {"name": 'Onion', "type": 'bulb', "quantity": 3},
  {"name": 'Chard', "type": 'leaf', "quantity": 3},
  {"name": 'Runner beans', "type": 'legume', "quantity": 8}]
    test_input_type = 'leaf'
    expected = 3
    result = count_veg(test_input_veg, test_input_type)
    assert result == expected

def test_if_list_and_type_are_empty_return_invalid(): 
    test_input_veg = []
    test_input_type = ''
    expected = 'Invalid type'

    result = count_veg(test_input_veg, test_input_type)

    assert result == expected

def test_if_only_list_empty_return_invalid(): 
    #arrange
    test_input_veg = []
    test_input_type = 'root'
    expected = 'Invalid list'

    #act 
    result = count_veg(test_input_veg, test_input_type)

    assert result == expected
    
def test_if_only_type_is_empty_return_invalid(): 
    #arrange
    test_input_veg = [{"name": 'Parsnip', "type": 'root', "quantity": 4}, 
                      {"name": 'Carrot', "type": 'root', "quantity": 5}]
    test_input_type = ''
    expected = 'Invalid type'

    #act 
    result = count_veg(test_input_veg, test_input_type)

    assert result == expected

def test_if_invalid_veg_typ_return_invalid(): 
    #arrange
    test_input_veg = [{"name": 'Parsnip', "type": 'root', "quantity": 4}, 
                      {"name": 'Carrot', "type": 'root', "quantity": 5}]
    test_input_type = 'fruit'
    expected = 'Invalid type'

    #act 
    result = count_veg(test_input_veg, test_input_type)

    assert result == expected



    
   