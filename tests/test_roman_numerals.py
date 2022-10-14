from roman_numerals.roman_numerals import RomanNumeralTranslator

# test all single roman numeral symbols


def test_translate_i():
    translator = RomanNumeralTranslator()

    result = translator.translate('I')
    assert result == 1


def test_translate_v():
    translator = RomanNumeralTranslator()

    result = translator.translate('V')
    assert result == 5


def test_translate_x():
    translator = RomanNumeralTranslator()

    result = translator.translate('X')
    assert result == 10


def test_translate_l():
    translator = RomanNumeralTranslator()

    result = translator.translate('L')
    assert result == 50


def test_translate_c():
    translator = RomanNumeralTranslator()

    result = translator.translate('C')
    assert result == 100


def test_translate_d():
    translator = RomanNumeralTranslator()

    result = translator.translate('D')
    assert result == 500


def test_translate_m():
    translator = RomanNumeralTranslator()

    result = translator.translate('M')
    assert result == 1000


def test_validate_each_numeral():
    # By design, a non-Roman numeral will not be translated, hence
    # the translation result will be None.
    translator = RomanNumeralTranslator()

    result = translator.translate('J')
    assert result is None


def test_lower_case_single_input():
    translator = RomanNumeralTranslator()

    result = translator.translate('i')
    assert result == 1


def test_transform_multi_numerals():
    # Translate Roman combined numerals to series of numbers
    # and calculate them
    translator = RomanNumeralTranslator()

    result = translator.calculate_numeral('II')
    assert result == 2

    result = translator.calculate_numeral('XX')
    assert result == 20

    result = translator.calculate_numeral('DX')
    assert result == 510

    result = translator.calculate_numeral('MDCLXVI')
    assert result == 1666


def test_partial_invalid_multi_numerals():
    # If we cannot summarize the values because of one or more illegal
    # numerals, we want the result to be None.

    translator = RomanNumeralTranslator()

    result = translator.calculate_numeral('Ij')
    assert result is None


def test_fully_invalid_multi_numerals():
    # If we cannot summarize the values because of one or more illegal
    # numerals, we want the result to be None.

    translator = RomanNumeralTranslator()

    result = translator.calculate_numeral('ajb')
    assert result is None


def test_lower_case_multi_input():
    translator = RomanNumeralTranslator()

    result = translator.calculate_numeral('xvi')
    assert result == 16


def test_invalid_multiples_of_5():
    # Multiples of 5 (and 50, 500) are not allowed,
    # because they would be a duplicate of the next Roman numeral.

    translator = RomanNumeralTranslator()

    result = translator.validate_multinumerals('vv')
    assert result is False

    result = translator.validate_multinumerals('ll')
    assert result is False

    result = translator.validate_multinumerals('dd')
    assert result is False

    result = translator.validate_multinumerals('cxvvi')
    assert result is False


def test_valid_multiples_of_5():
    translator = RomanNumeralTranslator()

    result = translator.validate_multinumerals('cxxvi')
    assert result is True


def test_subtractive_notation():
    # Valid combinations are: IV, IX, XL, XC, CD, CM
    translator = RomanNumeralTranslator()

    result = translator.calculate_numeral('iv')
    assert result == 4

    result = translator.calculate_numeral('ix')
    assert result == 9

    result = translator.calculate_numeral('xl')
    assert result == 40

    result = translator.calculate_numeral('xc')
    assert result == 90

    result = translator.calculate_numeral('cd')
    assert result == 400

    result = translator.calculate_numeral('cm')
    assert result == 900

# TODO: Add exception handling: illegal combinations
#       like 'VV', 'IL'.
# TODO: Transform from Arabic numbers to Roman numerals.
# TODO: Enable the library to only validate Roman numerals.
