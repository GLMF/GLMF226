from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
from typing import Tuple
import sys


def shellExit() -> None:
    print('Au revoir !')    
    sys.exit(0)

def myShell(promptChr : str = '>>>') -> None:
    MyCompleter = WordCompleter(['quit', 'exit', 'get', 'set'])
    while True:
        try:
            result = prompt(
                message=f'{promptChr} ',
                history=FileHistory('history.txt'),
                auto_suggest=AutoSuggestFromHistory(),
                completer=MyCompleter,
                complete_while_typing=True
            )
            print(f'Vous avez saisi : {result}')
            if result == 'quit' or result == 'exit':
                shellExit()
        except KeyboardInterrupt:
            shellExit()


if __name__ == '__main__':
    myShell()
