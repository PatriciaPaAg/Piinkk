from tracemalloc import start
from antlr4.error.ErrorListener import ErrorListener

class PiinkkErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError(f"line {line}:{column} {msg}")
