class RomanNumeralTranslator:
    def translate(self, roman_number):
        roman_number_table = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100,
                              'd': 500, 'm': 1000}

        return roman_number_table.get(roman_number)

    def calculate_multi_numbers(self, roman_number):
        translation_list = []
        answer = 0
        for symbol in roman_number:
            translation_list.append(self.translate(symbol))

        answer = sum((i) for i in translation_list)

        return answer
