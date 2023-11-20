from antlr4 import *
from PiinkkListener import PiinkkListener
from piinkkLoader import piinkkLoader

class PiinkkListenerExt(PiinkkListener):

    # Enter a parse tree produced by PiinkkParser#prog.
    def enterProg(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#prog.
    def exitProg(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#type0.
    def enterType0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#type0.
    def exitType0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#array0.
    def enterArray0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#array0.
    def exitArray0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#if0.
    def enterIf0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#if0.
    def exitIf0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#while0.
    def enterWhile0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#while0.
    def exitWhile0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#for0.
    def enterFor0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#for0.
    def exitFor0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#var0.
    def enterVar0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#var0.
    def exitVar0(self, ctx):
        pass

    # Enter a parse tree produced by PiinkkParser#vars0.
    def enterVars0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#vars0.
    def exitVars0(self, ctx):
        pass

    def enterVars1(self, ctx):
        vars_info = ctx.getText().split(':')
        vars_type = vars_info[0]
        vars_info = vars_info[1].split(',')
        for _ in range(len(vars_info)):
            #  If the next element is an array
            if vars_info[0].find('[') != -1:
                vars_info_arr = vars_info[0].split('[')
                var_name = vars_info_arr[0]
                var_arr_size = vars_info_arr[1][:-1]
                piinkkLoader.dirFun['global']['variables'][var_name] = {'type': vars_type, 'size': var_arr_size}
            else:
                var_name = vars_info[0]
                piinkkLoader.dirFun['global']['variables'][var_name] = {'type': vars_type}
            vars_info.pop(0)

    # Exit a parse tree produced by PiinkkParser#vars1.
    def exitVars1(self, ctx):
        pass

    # Enter a parse tree produced by PiinkkParser#expresion0.
    def enterExpresion0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#expresion0.
    def exitExpresion0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#exp0.
    def enterExp0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#exp0.
    def exitExp0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#termino0.
    def enterTermino0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#termino0.
    def exitTermino0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#factor0.
    def enterFactor0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#factor0.
    def exitFactor0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#bloque0.
    def enterBloque0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#bloque0.
    def exitBloque0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#estatuto0.
    def enterEstatuto0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#estatuto0.
    def exitEstatuto0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#asignacion0.
    def enterAsignacion0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#asignacion0.
    def exitAsignacion0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#escri.
    def enterEscri(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#escri.
    def exitEscri(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#escritura0.
    def enterEscritura0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#escritura0.
    def exitEscritura0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#return0.
    def enterReturn0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#return0.
    def exitReturn0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#fun0.
    def enterFun0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#fun0.
    def exitFun0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#body0.
    def enterBody0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#body0.
    def exitBody0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#start.
    def enterStart(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#start.
    def exitStart(self, ctx):
        pass
