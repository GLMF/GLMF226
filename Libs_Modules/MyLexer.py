from pygments.lexer import RegexLexer
from pygments.token import *

class MyLexer(RegexLexer):
    name = 'MyLanguage'
    aliases = ['myl']
    filenames = ['*.myl']

    tokens = {
       'root': [
           (r'(exit|quit|get|set)\b', Keyword),
           (r'(time|weather|wind)\b', String)
       ]
    }
