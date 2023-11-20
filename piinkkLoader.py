from ast import operator
from semanticCube import *
from collections import defaultdict

class PiinkkLoader():
    def __init__(self):
        self.operator_stack = []
        self.type_stack = []
        self.operand_stack = []
        self.jump_stack = []
        self.symbol_table = defaultdict(lambda:{'variables':{}})
        self.current_scope = 'global'

    def set_current_scope(self, scope_name):
        self.current_scope = scope_name

    def variableCheck(self, name):
        if name in self.symbol_table['global']['variables']:
            self.stopExecution(f'Variable \'{name}\' is already declared in global scope.')
        else:
            if name in self.symbol_table[self.current_scope]['variables']:
                self.stopExecution(f'Variable \'{name}\' is already declared in current scope.')

    def stopExecution(self, errorType):
        print(errorType)
        exit()

piinkkLoader = PiinkkLoader()







# {'global': {'variables': {'i': {'type': 'int'}}}
#  'function1': {'variables': {'x': {'type': 'int'}}, 'type': 'void' }
#  'function2': {'variables': {'y': {'type': 'int'}}, 'type': 'void' }
# }