class RomanNumeralTranslator:
    """ Translate Roman numerals into Arabic numbers.

    This module is used to translate Roman numerals into Arabic numbers.
    """

    def _translate(self, roman_numeral):
        """Translate a single Roman numeral into an Arabic number.

        Args:
            roman_numeral (string): a single roman numeral

        Returns:
            int: Arabic number - representing the value of the Roman
            numeral
        """

        roman_numeral_table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                               'D': 500, 'M': 1000}

        return roman_numeral_table.get(roman_numeral.upper())

    def _validate_multinumerals(self, multinumeral):
        """Check if multinumeral is a valid Roman numeral.

        Check for invalid two-numeral combinations in a Roman numeral.

        Args:
            multinumeral (string): Roman numeral (single or multinumeral)

        Returns:
            boolean: True if valid, else False.
        """

        invalid_multinumerals = ['vv', 'll', 'dd',
                                 'iiii', 'xxxx', 'cccc', 'mmmm']
        if any(i in multinumeral for i in invalid_multinumerals):
            return False
        else:
            return True

    def calculate_numeral(self, numeral):
        """Calculate the value of a Roman numeral.

        Calculate the Arabic number that represents a Roman single or
        multinumeral.

        Args:
            numeral (string): A Roman single or multinumeral.

        Returns:
            int: Arabic number representing the Roman numeral,
            or None when translation was not possible.
        """

        translation_list = []
        for symbol in numeral:
            translation_list.append(self._translate(symbol))

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
