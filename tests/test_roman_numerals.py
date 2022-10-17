import pytest

from roman_numerals.roman_numerals import RomanNumeralTranslator


@pytest.mark.parametrize("singlenumeral, arabic",
                         [('I', 1),
                          ('V', 5),
                          ('X', 10),
                          ('L', 50),
                          ('C', 100),
                          ('D', 500),
                          ('M', 1000)])
def test_translate_single_numeral(singlenumeral, arabic):
    translator = RomanNumeralTranslator()

    result = translator._translate(singlenumeral)
    assert result == arabic


def test_validate_each_numeral():
    # By design, a non-Roman numeral will not be translated, hence
    # the translation result will be None.
    translator = RomanNumeralTranslator()

    result = translator._translate('J')
    assert result is None


def test_lower_case_single_input():
    translator = RomanNumeralTranslator()

    result = translator._translate('i')
    assert result == 1


@pytest.mark.parametrize("multinumeral, arabic",
                         [('II', 2),
                          ('XX', 20),
                          ('DX', 510),
                          ('MDCLXVI', 1666)])
def test_transform_multi_numerals(multinumeral, arabic):
    translator = RomanNumeralTranslator()

    result = translator.calculate_numeral(multinumeral)
    assert result == arabic


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


@pytest.mark.parametrize("multinumeral", ['vv', 'll', 'dd', 'cxvvi'])
def test_invalid_multiples_of_5(multinumeral):
    # Multiples of 5 (and 50, 500) are not allowed,
    # because they would be a duplicate of the next Roman numeral.

    translator = RomanNumeralTranslator()

    result = translator._validate_multinumerals(multinumeral)
    assert result is False


def test_valid_multiples_of_5():
    translator = RomanNumeralTranslator()

    result = translator._validate_multinumerals('cxxvi')
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
