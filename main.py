def int_to_roman(num):
    numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman_equal = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    i = 12
    roman_numeral= " "
    while num != 0:
        if numbers[i] <= num:
            roman_numeral += roman_equal[i]
            num = num - numbers[i]
        else:
            i -= 1
    return roman_numeral
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
