class RomanNumeralTranslator:
    def translate(self, roman_number):

        roman_number_table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                              'D': 500, 'M': 1000}

        return roman_number_table.get(roman_number.upper())

    def calculate_multi_numbers(self, roman_number):
        translation_list = []
        result = 0
        for symbol in roman_number:
            translation_list.append(self.translate(symbol))

        try:
            result = sum((i) for i in translation_list)
            return result
        except TypeError:
            return None
