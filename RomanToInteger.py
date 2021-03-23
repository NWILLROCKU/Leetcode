s = 'IV'

def convertRomDig(roman):
    switcher = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    return switcher.get(roman, 0)

num = 0
digit = convertRomDig(s[0])
for i in range(1, len(s)):
    prev_digit = digit
    digit = convertRomDig(s[i])
    if prev_digit < digit:
        num -= prev_digit
    else:
        num += prev_digit
num += digit
