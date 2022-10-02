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


def test_transform_multi_numbers():
    # Translate Roman combined numerals to series of numbers
    # and calculate them
    translator = RomanNumeralTranslator()

    result = translator.calculate_multi_numbers('II')
    assert result == 2

    result = translator.calculate_multi_numbers('XX')
    assert result == 20

    result = translator.calculate_multi_numbers('DX')
    assert result == 510

    result = translator.calculate_multi_numbers('MDCLXVI')
    assert result == 1666


def test_partial_invalid_multi_numbers():
    translator = RomanNumeralTranslator()

    result = translator.calculate_multi_numbers('Ij')
    assert result is None


def test_lower_case_multi_input():
    translator = RomanNumeralTranslator()

    result = translator.calculate_multi_numbers('xvi')
    assert result == 16


# TODO: Add exception handling: illegal characters, illegal combinations
#       like 'VV', 'IL'.
# TODO: Add handling of smaller numerals that make subsequent larger
#       numeral smaller (like IV, IX, XM).
# TODO: Transform from Arabic numbers to Roman numbers.
