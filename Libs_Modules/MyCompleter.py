from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.document import Document
from prompt_toolkit.completion.base import CompleteEvent
from typing import Tuple


class MyCompleter(Completer):
    CMD : Tuple[str] = ('exit', 'quit', 'get', 'set')
    OTHER : Tuple[str] = ('time', 'weather', 'wind')

    def get_completions(self, document : Document, complete_event : CompleteEvent) -> Completion:
        for cmd, color in zip((MyCompleter.CMD + MyCompleter.OTHER), (('bg:ansiblack fg:ansired',) * len(MyCompleter.CMD)) + (('bg:ansiyellow fg:ansiblack',) * len(MyCompleter.OTHER))):
            last_word = document.get_word_under_cursor()
            if cmd.startswith(last_word) and not last_word == '':
                yield Completion(cmd, start_position=-len(last_word), style=color)
