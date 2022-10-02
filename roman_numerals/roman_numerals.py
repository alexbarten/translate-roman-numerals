class RomanNumeralTranslator:
    def translate(self, roman_number):

        roman_number_table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                              'D': 500, 'M': 1000}

        return roman_number_table.get(roman_number.upper())

    def calculate_multi_numbers(self, roman_number):
        translation_list = []
        for symbol in roman_number:
            translation_list.append(self.translate(symbol))

        try:
            pos = 0
            for number in translation_list:
                if pos > 0:
                    if translation_list[pos-1] < translation_list[pos]:
                        translation_list[pos-1] = -translation_list[pos-1]
                pos += 1
            return sum((number) for number in translation_list)

        except TypeError:
            return None
