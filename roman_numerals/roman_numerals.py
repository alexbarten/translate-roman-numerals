class RomanNumeralTranslator:
    """ Translate Roman numbers into Arabic numbers.

    This module is used to translate Roman numbers into Arabic numbers.
    """

    def translate(self, roman_number):
        """Translate a single Roman numeral into an Arabic number.

        Args:
            roman_number (string): a single roman numeral

        Returns:
            int: Arabic number - representing the value of the Roman
            numeral
        """

        roman_number_table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                              'D': 500, 'M': 1000}

        return roman_number_table.get(roman_number.upper())

    def validate_multinumerals(self, multinumeral):
        invalid_doubles = ['vv', 'll', 'dd']
        if any(i in multinumeral for i in invalid_doubles):
            return False
        else:
            return True

    def calculate_numeral(self, numeral):
        translation_list = []
        for symbol in numeral:
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
