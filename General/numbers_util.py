import re
def string_to_number(string_number):
    multipliers = {
        'k':10**3,
        'm': 10 **6,
        'b': 10**9
    }
    string_number = str(string_number).replace(',', '')
    string_number = str(string_number).replace(' ', '')
    if string_number[-1] in multipliers:
        return int(float(string_number[:-1]) * multipliers[string_number[-1]])
    else:
        return int(string_number)

