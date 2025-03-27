# 1) Write a python class to convert an integer into a roman numeral and viceversa

class Roman:
    def __init__(self):
        self.roman = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        self.integer = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }

    def int_to_roman(self, num):
        result = ''
        for key in sorted(self.roman.keys(), reverse=True):
            while num >= key:
                result += self.roman[key]
                num -= key
        return result
    
    def roman_to_int(self, roman):
        result = 0
        i = 0
        while i < len(roman):
            if i+1 < len(roman) and roman[i:i+2] in self.integer:
                result += self.integer[roman[i:i+2]]
                i += 2
            else:
                result += self.integer[roman[i]]
                i += 1
        return result
    
    def convert(self, value):
        if isinstance(value, int):
            return self.int_to_roman(value)
        elif isinstance(value, str):
            return self.roman_to_int(value)
        else:
            return 'Invalid input'
        
# Test
r = Roman()
print(r.convert(354)) # CCCLIV
print(r.convert('CCCLIV')) # 354