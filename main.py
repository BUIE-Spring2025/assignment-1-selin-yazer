def int_to_roman(num):
    num_to_roman = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
        (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
        (5, "V"), (4, "IV"), (1, "I")
    ]

    roman_numeral = " "
    for value, symbol in num_to_roman:
        while num >= value:
            roman_numeral += symbol
            num -= value

    return roman_numeral
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
