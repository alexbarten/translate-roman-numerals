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

        self._create_list_of_arabic_numbers(multinumeral)
        prev_number = 0

        for number in self.transformed_numbers:
            if prev_number in [5, 50, 500]:
                if number > prev_number:
                    return False
            prev_number = number

        return True

    def _create_list_of_arabic_numbers(self, numeral):
        """Tranform each Roman numeral in an Arabic number and store it
        into a list.

        Args:
            numeral (string): Roman numeral or multinumeral
        """

        self.transformed_numbers = []
        for symbol in numeral:
            self.transformed_numbers.append(self._translate(symbol))

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

        self._create_list_of_arabic_numbers(numeral)

        try:
            pos = 0
            for number in self.transformed_numbers:
                if pos > 0:
                    if self.transformed_numbers[pos-1] < \
                       self.transformed_numbers[pos]:
                        self.transformed_numbers[pos-1] = \
                         -self.transformed_numbers[pos-1]
                pos += 1
            return sum((number) for number in self.transformed_numbers)

        except TypeError:
            return None
