
from collections import defaultdict

class  MemoryManage:
    # Constants
    GLOBAL_INIT_ADD = 500
    GLOBAL_FIN_ADD = 799
    LOCAL_INIT_ADD = 800
    LOCAL_FIN_ADD = 1099
    TEMP_INIT_ADD = 1100
    TEMP_FIN_ADD = 1399
    CTE_INIT_ADD = 1400
    CTE_FIN_ADD = 1599

    def __init__(self):
        self.count = 0
        self.globals = defaultdict(lambda: {'count': 0, 'iniAdd': None, 'finAdd': None})
        self.locals = defaultdict(lambda: {'count': 0, 'iniAdd': None, 'finAdd': None})
        self.temps = defaultdict(lambda: {'count': 0, 'iniAdd': None, 'finAdd': None})
        self.ctes = defaultdict(lambda: {'count': 0, 'iniAdd': None, 'finAdd': None})
        self.setValues()
    
    def setValues(self):
        self.globals['int']['iniAdd'] = 5000
        self.globals['int']['finAdd'] = 5999
        self.globals['float']['iniAdd'] = 6000
        self.globals['float']['finAdd'] = 6999
        self.globals['bool']['iniAdd'] = 7000
        self.globals['bool']['finAdd'] = 7999
        self.locals['int']['iniAdd'] = 8000
        self.locals['int']['finAdd'] = 8999
        self.locals['float']['iniAdd'] = 9000
        self.locals['float']['finAdd'] = 9999
        self.locals['bool']['iniAdd'] = 10000
        self.locals['bool']['finAdd'] = 10999
        self.temps['int']['iniAdd'] = 11000
        self.temps['int']['finAdd'] = 11999
        self.temps['float']['iniAdd'] = 12000
        self.temps['float']['finAdd'] = 12999
        self.temps['bool']['iniAdd'] = 13000
        self.temps['bool']['finAdd'] = 13999
        self.ctes['int']['iniAdd'] = 14000
        self.ctes['int']['finAdd'] = 14999
        self.ctes['float']['iniAdd'] = 15000
        self.ctes['float']['finAdd'] = 15999

    def getNewAddress(self, memory_scope, data_type):
        if memory_scope == 'global':
            scope = self.globals
        elif memory_scope == 'temp':
            scope = self.temps
        elif memory_scope == 'ctes':
            scope = self.ctes
        else:
            scope = self.locals
        newAddress = scope[data_type]['iniAdd'] + scope[data_type]['count']
        if newAddress > scope[data_type]['finAdd']:
            raise Exception('Memory overflow')
        scope[data_type]['count'] += 1
        return newAddress
    
    # def getAdress(self, memory_scope, data_type):
    #     if memory_scope == 'global':
    #         scope = self.globals
    #     elif memory_scope == 'temp':
    #         scope = self.temps
    #     elif memory_scope == 'ctes':
    #         scope = self.ctes
    #     else:
    #         scope = self.locals

    #     newAddress = scope[data_type]['iniAdd'] + scope[data_type]['count']

    #     if newAddress > scope[data_type]['finAdd']:
    #         raise Exception('Memory overflow')
    #     scope[data_type]['count'] += 1

    #     return newAddress

    
    def resetCountLocal(self):
        self.locals['int']['count'] = 0
        self.locals['float']['count'] = 0
        self.locals['bool']['count'] = 0
    
    def resetCountTemp(self):
        self.temps['int']['count'] = 0
        self.temps['float']['count'] = 0
        self.temps['bool']['count'] = 0



memoryManage = MemoryManage()