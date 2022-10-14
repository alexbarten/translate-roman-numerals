# translate-roman-numerals

A Python class to translate Roman numerals to Arabic numbers.

## Rules

This class implements the [_standard form_ of Roman numerals](https://en.wikipedia.org/wiki/Roman_numerals#Standard_form).

## How to use it

Import the library into your Python module:

```python
from roman_numerals import RomanNumeralTranslator
```

Or

```python
import roman_numerals
```

The `RomanNumeralTranslator` class exposes one method: `calculate_numeral`.

This method takes any Roman numeral as its input:

```python
result = calculate_numeral('C')
```

Or

```python
result = calculate_numeral('MDCLXVI')
```

If the Roman numeral is not valid, the returned result will be `None`.

The module does not return exceptions.

## Future ideas and improvements

TODO: Refactor tests with pytest (combine calls).
TODO: Add exception handling: illegal combinations
      like 'VV', 'IL'. We should still give back None, but we might
      raise an exception or add a return code as well...
TODO: Transform from Arabic numbers to Roman numerals.
TODO: Enable the library to only validate Roman numerals.
