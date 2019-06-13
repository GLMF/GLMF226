from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from MyCompleter import MyCompleter
from prompt_toolkit.lexers import PygmentsLexer
from MyLexer import MyLexer
from prompt_toolkit.styles import Style
from time import gmtime, strftime
import sys


def shellExit() -> None:
    print('Au revoir !')    
    sys.exit(0)

def getRprompt() -> str:
    return strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

def myShell(promptChr : str = '>>>') -> None:
    myStyle = Style.from_dict({
        'rprompt': 'bg:#12f #fff',
    })

    while True:
        try:
            result = prompt(
                message=f'{promptChr} ',
                history=FileHistory('history.txt'),
                auto_suggest=AutoSuggestFromHistory(),
                completer=MyCompleter(),
                complete_while_typing=True,
                lexer=PygmentsLexer(MyLexer),
                rprompt=getRprompt,
                style=myStyle
            )
            print(f'Vous avez saisi : {result}')
            if result == 'quit' or result == 'exit':
                shellExit()
        except KeyboardInterrupt:
            shellExit()


if __name__ == '__main__':
    myShell()
