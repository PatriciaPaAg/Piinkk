from antlr4 import *
from PiinkkLexer import PiinkkLexer
from PiinkkListenerExt import PiinkkListenerExt
from PiinkkParser import PiinkkParser
from piinkkLoader import piinkkLoader
from piinkkErrorListener import PiinkkErrorListener

filename = 'testRight.pink'
test = ''
with open(filename, 'r') as file:
    test = file.readlines()

lexer = PiinkkLexer(InputStream(''.join(test)))
stream = CommonTokenStream(lexer)
parser = PiinkkParser(stream)

error_listener = PiinkkErrorListener()
parser.removeErrorListeners()
parser.addErrorListener(error_listener)

try: 
    tree = parser.prog()
    listener = PiinkkListenerExt()
    ParseTreeWalker().walk(listener, tree)
    print('\nPrints del main')
    print(piinkkLoader.symbol_table)
    print('hola mundo')

except SyntaxError as e:
    print(F'Syntax ERROR: {e}')