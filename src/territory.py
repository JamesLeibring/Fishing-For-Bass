3 # The Location Class
class Territory:
    def __init__(self) -> None:
        pass

# Turn a integer into a Roman Numeral
def roman(number):
    ret_val = ""
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    while number:
        div = number // num[i]
        number %= num[i]
        while div:
            ret_val += sym[i]
            div -= 1
        i -= 1
    return ret_val
