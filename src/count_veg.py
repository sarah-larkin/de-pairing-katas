def count_veg(veg, type):
    total = 0 
    for item in veg: 
        if item["type"] == 'root':
            total += item['quantity']
            return item['quantity']
    return 0 
