from prompt_toolkit.validation import Validator
from prompt_toolkit import prompt
import regex


def isDate(value : str) -> bool:
    return regex.match('^(([0-2][0-9])|(3[0-1]))/((0[0-9])|(1[0-2]))/\d{4}$', value)

dateValidator = Validator.from_callable(
    isDate,
    error_message='Veuillez saisir une date valide (format jj/mm/aaaa)',
    move_cursor_to_end=True
)

result = prompt('Saisissez une date au format jj/mm/aaaa : ', validator=dateValidator)
print(f'Date saisie : {result}')
