class RomanConverter:

    LITERALS = {"I": 1, "IV": 4, "V": 5, "IX": 9,
                "X": 10, "XL": 40, "L": 50, "XC": 90,
                "C": 100, "CD": 400, "D": 500, "CM": 900,
                "M": 1000,
                1: "I", 4: "IV", 5: "V", 9: "IX",
                10: "X", 40: "XL", 50: "L", 90: "XC",
                100: "C", 400: "CD", 500: "D", 900: "CM",
                1000: "M" }
                        
    REDUCE_LITERALS = ["CM", "CD", "XC", "XL", "IX", "IV"]
    
    @classmethod
    def convert(cls, number):
        """
        Returns converted number depending of given number.
        If arabic is given, roman is returned and vice versa.
        
        Params:
            -- int / string
        Return:
            -- string / int
        """
  
        if not cls.validate(number):
            return False
        
        if isinstance(number, str):
            # initial setting
            arabic = 0
            roman = number.upper()
            
            while roman:
                if len(roman) > 1:
                    if roman[0:2] in cls.REDUCE_LITERALS:
                        arabic += cls.LITERALS[roman[0:2]]
                        roman = roman[2:]
                    else:
                        arabic += cls.LITERALS[roman[0]]
                        roman = roman[1:]
                else:
                    arabic += cls.LITERALS[roman]
                    roman = None
            
            return arabic
        
        else:
            # initial setting
            roman = ''
            arabic = number
            
            values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
            
            while arabic:
                if arabic >= values[0]:
                    arabic -= values[0]
                    roman += cls.LITERALS[values[0]]
                else:
                    values.pop(0)
            
            return roman
     
    @classmethod
    def validate(cls, number):
        """
        Returns True if number is a valid for conversion,
        otherwise returns False.
        
        Params:
            -- int / string

        Return:
            -- boolean
        """
    
        
        if isinstance(number, str) and number:
            from re import match as re_match
            
            matching_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
            
            if re_match(matching_pattern, number):
                return True
            else:
                return False
        
        elif isinstance(number, int):
            return 0 < number and number < 4000
        
        else:
            return False