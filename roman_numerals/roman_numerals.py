class RomanNumeralTranslator:
    def translate(self, roman_number):
        answer = None
        if roman_number == 'i':
            answer = 1
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

    def translate_two(self, roman_number):
        translation_list = []
        for symbol in roman_number:
            translation_list.append(symbol)

        return translation_list
