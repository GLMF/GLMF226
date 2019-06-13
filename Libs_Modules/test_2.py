from prompt_toolkit import prompt
import sys


def shellExit() -> None:
    print('Au revoir !')    
    sys.exit(0)

def myShell(promptChr : str = '>>>') -> None:
    while True:
        try:
            result = prompt(f'{promptChr} ')
            print(f'Vous avez saisi : {result}')
            if result == 'quit' or result == 'exit':
                shellExit()
        except KeyboardInterrupt:
            shellExit()


if __name__ == '__main__':
    myShell()
