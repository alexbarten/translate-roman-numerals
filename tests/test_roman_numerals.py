import pytest

from roman_numerals.roman_numerals import RomanNumeralTranslator

TRANSLATOR = RomanNumeralTranslator()


@pytest.mark.parametrize('singlenumeral, arabic',
                         [('I', 1),
                          ('V', 5),
                          ('X', 10),
                          ('L', 50),
                          ('C', 100),
                          ('D', 500),
                          ('M', 1000)])
def test_translate_single_numeral(singlenumeral, arabic):
    result = TRANSLATOR._translate(singlenumeral)
    assert result == arabic


def test_validate_each_numeral():
    # By design, a non-Roman numeral will not be translated, hence
    # the translation result will be None.
    result = TRANSLATOR._translate('J')
    assert result is None


def test_lower_case_single_input():
    result = TRANSLATOR._translate('i')
    assert result == 1


@pytest.mark.parametrize('multinumeral', ['vv', 'll', 'dd', 'cxvvi'])
def test_invalid_multiples_of_5(multinumeral):
    # Multiples of 5 (and 50, 500) are not allowed,
    # because they would be a duplicate of the next Roman numeral.
    result = TRANSLATOR._validate_multinumerals(multinumeral)
    assert result is False


def test_invalid_equal_multiples_over_3():
    # Equal multiples of more than 3 numerals are not valid
    result = TRANSLATOR._validate_multinumerals('iiii')
    assert result is False


@pytest.mark.parametrize('multinumeral', ['vx', 'vl', 'ld', 'dm'])
def test_invalid_5_before_higher_number(multinumeral):
    # 'Fives' cannot be in front of a greater number.
    result = TRANSLATOR._validate_multinumerals(multinumeral)
    assert result is False


@pytest.mark.parametrize('small_subtractor', ['il', 'im', 'xd', 'xm'])
def test_non_allowed_subtractors(small_subtractor):
    # I cannot subtract from anything greater than X,
    # X not from greater than C.
    result = TRANSLATOR._validate_multinumerals(small_subtractor)
    assert result is False


def test_valid_multiples():
    result = TRANSLATOR._validate_multinumerals('cxxvi')
    assert result is True


@pytest.mark.parametrize('multinumeral, arabic',
                         [('II', 2),
                          ('XX', 20),
                          ('DX', 510),
                          ('MDCLXVI', 1666)])
def test_transform_multi_numerals(multinumeral, arabic):
    result = TRANSLATOR.calculate_numeral(multinumeral)
    assert result == arabic


@pytest.mark.parametrize('partial_invalid', ['Ij', '-X', 'C++', 'M*M'])
def test_partial_invalid_multi_numerals(partial_invalid):
    # If we cannot summarize the values because of one or more illegal
    # numerals, we want the result to be None.
    result = TRANSLATOR.calculate_numeral(partial_invalid)
    assert result is None


def test_fully_invalid_multi_numerals():
    # If we cannot summarize the values because of one or more illegal
    # numerals, we want the result to be None.
    result = TRANSLATOR.calculate_numeral('ajb')
    assert result is None


def test_lower_case_multi_input():
    result = TRANSLATOR.calculate_numeral('xvi')
    assert result == 16


@pytest.mark.parametrize('subtractor, sum',
                         [('IV', 4),
                          ('IX', 9),
                          ('XL', 40),
                          ('XC', 90),
                          ('CD', 400),
                          ('CM', 900)])
def test_subtractive_notation(subtractor, sum):
    result = TRANSLATOR.calculate_numeral(subtractor)
    assert result == sum
