class RomanNumeralTranslator:
    def translate(self, roman_number):
        answer = None
        roman_number_table = {'i': 1}
        if roman_number == 'i':
            answer = roman_number_table.get('i')
        elif roman_number == 'v':
            answer = 5
        elif roman_number == 'x':
            answer = 10
        elif roman_number == 'l':
            answer = 50
        elif roman_number == 'c':
            answer = 100
        elif roman_number == 'd':
            answer = 500
        elif roman_number == 'm':
            answer = 1000
        return answer

    def calculate_multi_numbers(self, roman_number):
        translation_list = []
        answer = 0
        for symbol in roman_number:
            translation_list.append(self.translate(symbol))

        answer = sum((i) for i in translation_list)

        return answer
