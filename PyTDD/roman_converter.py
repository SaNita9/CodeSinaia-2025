
def roman_converter(num):

    if not isinstance(num, int):
        return None
    
    if num >=4000 or num <=0:
        return None

    # if num == 1:
    #     return 'I'

    # if num == 5:
    #     return 'V'
    
    out = ''

    # while num >= 5: 
    #     out += 'V'
    #     num -=1
    

    # while num >= 1: 
    #     out += 'I'
    #     num -=1
    ROMAN_VALUES = [
        (1000, 'M'),
        (500, 'D'),
        (100, 'C'),
        (50, 'L'),
        (10, 'X'),
        (5, 'V'),
        (1, 'I')
    ]

    for (value, symbol) in ROMAN_VALUES:
        while num >= value: 
            out += symbol
            num -= value

    return out