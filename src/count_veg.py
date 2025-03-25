def count_veg(veg_list, veg_type):
    valid_types = ['root', 'leaf', 'legume', 'bulb', 'brassica']
    if veg_type not in valid_types:
        return 'Invalid type'
    if not veg_list:
        return 'Invalid list'
    total = 0
    for item in veg_list: 
        if item["type"] == veg_type:
            total += item['quantity']
            
    return total

