class RomanNumeralTranslator:
    def translate(self, roman_number):
        roman_number_table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                              'D': 500, 'M': 1000}

        return roman_number_table.get(roman_number)

    def calculate_multi_numbers(self, roman_number):
        translation_list = []
        answer = 0
        for symbol in roman_number:
            translation_list.append(self.translate(symbol))

        answer = sum((i) for i in translation_list)

        return answer
