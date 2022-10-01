from roman_numerals.roman_numerals import RomanNumeralTranslator

# test all single roman numeral symbols


def test_translate_i():
    translator = RomanNumeralTranslator()

    result = translator.translate('i')
    assert result == 1


def test_translate_v():
    translator = RomanNumeralTranslator()

    result = translator.translate('v')
    assert result == 5


def test_translate_x():
    translator = RomanNumeralTranslator()

    result = translator.translate('x')
    assert result == 10


def test_translate_l():
    translator = RomanNumeralTranslator()

    result = translator.translate('l')
    assert result == 50


def test_translate_c():
    translator = RomanNumeralTranslator()

    result = translator.translate('c')
    assert result == 100


def test_translate_d():
    translator = RomanNumeralTranslator()

    result = translator.translate('d')
    assert result == 500


def test_translate_m():
    translator = RomanNumeralTranslator()

    result = translator.translate('m')
    assert result == 1000


def test_transform_multi_numbers():
    # Translate Roman combined numerals to series of numbers
    # and calculate them
    translator = RomanNumeralTranslator()

    result = translator.calculate_multi_numbers('ii')
    assert result == 2

    result = translator.calculate_multi_numbers('xx')
    assert result == 20

    result = translator.calculate_multi_numbers('dx')
    assert result == 510

    result = translator.calculate_multi_numbers('mdclxvi')
    assert result == 1666
