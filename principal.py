from antlr4 import *
from PiinkkLexer import PiinkkLexer
from PiinkkListenerExt import PiinkkListenerExt
from PiinkkParser import PiinkkParser
from piinkkLoader import piinkkLoader

filename = 'testRight.pink'
test = ''
with open(filename, 'r') as file:
    test = file.readlines()

lexer = PiinkkLexer(InputStream(''.join(test)))
stream = CommonTokenStream(lexer)
parser = PiinkkParser(stream)
tree = parser.prog()
listener = PiinkkListenerExt()
ParseTreeWalker().walk(listener, tree)

print(piinkkLoader.dirFun)
print('hola mundo')

