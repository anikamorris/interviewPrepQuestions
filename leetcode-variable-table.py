test_case = 181

def isPalindrome(num):
    """
        :type num: int
        :rtype: bool
    """
    if num < 0 or (num % 10 == 0 and num != 0):
        return False
    
    num = str(num)
    i = 0
    while i < len(num) / 2:
        if num[i] != num[-i-1]:
            return False
        i += 1
    return True

# variable table
# --------------------
# | variable   | value |
# --------------------
# | num        | 181   | 
# | num        | "181" |
# | i          | 0     |
# | len(num)/2 | 1     |
# | num[0]     | "1"   |
# | num[-1]    | "1"   |
# | i          | 1     |


test_roman = 49

def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    roman_numeral = ""
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
    for i in range(len(values)):
        y = num // values[i]
        roman_numeral += y * symbols[i]
        num -= values[i] * y
    
    return roman_numeral

# variable table
# --------------------
# | variable      | value |
# --------------------
# | num           | 49    | 
# | roman_numeral | ""    |
# | i             | 0     |
# | values[i]     | 1000  |
# | y             | 0     |
# | roman_numeral | ""    |
# | num           | 49    |
# | i             | 1     |
# | values[i]     | 900   |
# | y             | 0     |
# | roman_numeral | ""    |
# | num           | 49    |
# | i             | 2     |
# | values[i]     | 500   |
# | y             | 0     |
# | roman_numeral | ""    |
# | num           | 49    |
# | i             | 3     |
# | values[i]     | 400   |
# | y             | 0     |
# | roman_numeral | ""    |
# | num           | 49    |
# | i             | 4     |
# | values[i]     | 100   |
# | y             | 0     |
# | roman_numeral | ""    |
# | num           | 49    |
# | i             | 5     |
# | values[i]     | 90    |
# | y             | 0     |
# | roman_numeral | ""    |
# | num           | 49    |
# | i             | 6     |
# | values[i]     | 50    |
# | y             | 0     |
# | roman_numeral | ""    |
# | num           | 49    |
# | i             | 7     |
# | values[i]     | 40    |
# | y             | 1     |
# | roman_numeral | "XL"  |
# | num           | 9     |
# | i             | 8     |
# | values[i]     | 10    |
# | y             | 0     |
# | roman_numeral | "XL"  |
# | num           | 9     |
# | i             | 9     |
# | values[i]     | 9     |
# | y             | 1     |
# | roman_numeral | "XLIX"|
# | num           | 0     |
# | i             | 10    |
# | values[i]     | 5     |
# | y             | 0     |
# | roman_numeral | "XLIX"|
# | num           | 0     |
# | i             | 11    |
# | values[i]     | 4     |
# | y             | 0     |
# | roman_numeral | "XLIX"|
# | num           | 0     |
# | i             | 12    |
# | values[i]     | 1     |
# | y             | 0     |
# | roman_numeral | "XLIX"|
# | num           | 0     |




