from prompt_toolkit.shortcuts import button_dialog
from typing import Any

def menu() -> Any:
    result = button_dialog(
        title='Exemple de boîte de dialogue',
        text='Veuillez répondre à la question suivante:\nContinuer le programme?',
        buttons=[
            ('Oui', True),
            ('Non', False),
            ('Euh...', None)
        ]
    )
    return result


if __name__ == '__main__':
    result = menu()
    print(f'Choix de l\'utilisateur : {result}')
