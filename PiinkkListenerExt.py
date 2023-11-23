from antlr4 import *
from PiinkkListener import PiinkkListener
from piinkkLoader import piinkkLoader
from semanticCube import *

class PiinkkListenerExt(PiinkkListener):

    # Enter a parse tree produced by PiinkkParser#prog.
    def enterProg(self, ctx):
        #agregar nombre de programa and type to Symbol Table
        #crear dir fun, inecesario porque ya esta creado
        #piinkkLoader.symbol_table['nameProg'= ]
        piinkkLoader.pendientes.append('agregar nombre de programa and type to Symbol Table')
        pass

    # Exit a parse tree produced by PiinkkParser#prog.
    def exitProg(self, ctx):
        piinkkLoader.pendientes.append('delete dir fun and current variable global, or empty them')
        #delete dir fun (necesario?) and current varTable (global)
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
        var_info = ctx.getText()
        piinkkLoader.operand_stack.append(var_info)
        # AQUI SE PUEDE PONER LO DE LOS NUMEROS ENTEROS O FLOAT
        if piinkkLoader.isNumber(var_info) == 'int':
            piinkkLoader.type_stack.append('int')
        elif piinkkLoader.isNumber(var_info) == 'float':
            piinkkLoader.type_stack.append('float')
        else:
            var_type = piinkkLoader.getType(var_info)
            piinkkLoader.type_stack.append(var_type)
        print('Operand Stack')
        print(piinkkLoader.operand_stack)

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
        vars_type, vars_info = vars_info[0], vars_info[1].split(',')
        scope = piinkkLoader.current_scope
        for var_info in vars_info:
            #  If the next element is an array
            if '[' in var_info:
                var_name, var_arr_size = var_info.split('[')
                var_arr_size = int(var_arr_size.rstrip(']'))
                piinkkLoader.variableCheck(var_name)
                piinkkLoader.symbol_table[scope]['variables'][var_name] = {'type': vars_type, 'size': var_arr_size}
            else:
                var_name = var_info
                piinkkLoader.variableCheck(var_name)
                piinkkLoader.symbol_table[scope]['variables'][var_name] = {'type': vars_type}            

    # Exit a parse tree produced by PiinkkParser#vars1.
    def exitVars1(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#expresion0.
    def enterExpresion0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#expresion0.
    def exitExpresion0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#expresion1.
    def enterExpresion1(self, ctx):
        operator_info = ctx.getText()
        for operator in ['==', '>', '<', '!=', '>=', '<=']:
            if operator in operator_info:
                piinkkLoader.operator_stack.append(operator)

    # Exit a parse tree produced by PiinkkParser#expresion1.
    def exitExpresion1(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#exp0.
    def enterExp0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#exp0.
    def exitExp0(self, ctx):
        Poper = piinkkLoader.operator_stack
        PilaO = piinkkLoader.operand_stack
        PilaT = piinkkLoader.type_stack
        if Poper:
            if Poper[-1] in ['==', '>', '<', '!=', '>=', '<=']:
                right_operand = PilaO.pop()
                right_type = PilaT.pop()
                left_operand = PilaO.pop()
                left_type = PilaT.pop()
                operator = Poper.pop()
                
                result_type = semantic_cube[left_type][right_type][operator]
                print(result_type)
                if(result_type == PiinkkError):
                    piinkkLoader.stopExecution(f'Type mismatch >') 
                temporal = piinkkLoader.getTemporal()
                PilaO.append(f't{temporal}')
                PilaT.append(result_type)
                piinkkLoader.addQuadruple([operator, left_operand, right_operand, f't{temporal}'])
                print(f'\t\t\t{operator}\t{left_operand}\t{right_operand}\tt{temporal}')
                print(f'\t\t\t{operator}\t{left_type}\t{right_type}\t{result_type}')
                piinkkLoader.temporal += 1



    # Enter a parse tree produced by PiinkkParser#exp1.
    def enterExp1(self, ctx):
        operator = ctx.getText()[0]
        piinkkLoader.operator_stack.append(operator)

    # Exit a parse tree produced by PiinkkParser#exp1.
    def exitExp1(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#termino0.
    def enterTermino0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#termino0.
    def exitTermino0(self, ctx):
        Poper = piinkkLoader.operator_stack
        PilaO = piinkkLoader.operand_stack
        PilaT = piinkkLoader.type_stack
        if Poper:
            if Poper[-1] in ['+', '-']:
                right_operand = PilaO.pop()
                right_type = PilaT.pop()
                left_operand = PilaO.pop()
                left_type = PilaT.pop()
                operator = Poper.pop()
                result_type = semantic_cube[left_type][right_type][operator]
                print(result_type)
                if(result_type == PiinkkError):
                    piinkkLoader.stopExecution(f'Type mismatch +')
                temporal = piinkkLoader.getTemporal()
                PilaO.append(f't{temporal}')
                PilaT.append(result_type)
                piinkkLoader.addQuadruple([operator, left_operand, right_operand, f't{temporal}'])
                print(f'\t\t\t{operator}\t{left_operand}\t{right_operand}\tt{temporal}')
                print(f'\t\t\t{operator}\t{left_type}\t{right_type}\t{result_type}')
                print(PilaO)
                piinkkLoader.temporal += 1
    

    # Enter a parse tree produced by PiinkkParser#termino1.
    def enterTermino1(self, ctx):
        operator = ctx.getText()[0]
        piinkkLoader.operator_stack.append(operator)

    # Exit a parse tree produced by PiinkkParser#termino1.
    def exitTermino1(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#factor0.
    def enterFactor0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#factor0.
    def exitFactor0(self, ctx):
        Poper = piinkkLoader.operator_stack
        PilaO = piinkkLoader.operand_stack
        PilaT = piinkkLoader.type_stack
        if Poper:
            if Poper[-1] in ['*', '/']:
                right_operand = PilaO.pop()
                right_type = PilaT.pop()
                left_operand = PilaO.pop()
                left_type = PilaT.pop()
                operator = Poper.pop()
                result_type = semantic_cube[left_type][right_type][operator]
                print(result_type)
                if(result_type == PiinkkError):
                    piinkkLoader.stopExecution(f'Type mismatch *') 
                temporal = piinkkLoader.getTemporal()
                PilaO.append(f't{temporal}')
                PilaT.append(result_type)
                piinkkLoader.addQuadruple([operator, left_operand, right_operand, f't{temporal}'])
                print(f'\t\t\t{operator}\t{left_operand}\t{right_operand}\tt{temporal}')
                print(f'\t\t\t{operator}\t{left_type}\t{right_type}\t{result_type}')
                piinkkLoader.temporal += 1


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
        piinkkLoader.clearStacks()

    # Exit a parse tree produced by PiinkkParser#asignacion0.
    def exitAsignacion0(self, ctx):
        assignTo = ctx.getText().split('=')[0]
        PilaO = piinkkLoader.operand_stack
        PilaT = piinkkLoader.type_stack
        assignThis = PilaO.pop()
        assignThis_type = PilaT.pop()
        assignTo_type = piinkkLoader.getType(assignTo)
        operator = '='
        result_type = semantic_cube[assignTo_type][assignThis_type][operator]
        print(PilaO)
        print(result_type)
        print(assignTo_type, assignThis_type, operator)
        if(result_type == PiinkkError):
            piinkkLoader.stopExecution(f'Type mismatch =') 
        piinkkLoader.addQuadruple([operator, assignThis, assignTo])
        print(f'\t\t\t{operator}\t{assignThis}\t{assignTo}')
        print(f'\t\t\t{operator}\t{assignThis_type}\t{assignTo_type}\t{result_type}')


    # Enter a parse tree produced by PiinkkParser#escritura0.
    def enterEscritura0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#escritura0.
    def exitEscritura0(self, ctx):
        pass


   # Enter a parse tree produced by PiinkkParser#escri.
    def enterEscri1(self, ctx):
        piinkkLoader.clearStacks()

    # Exit a parse tree produced by PiinkkParser#escri.
    def exitEscri1(self, ctx):
        impre = piinkkLoader.operand_stack.pop()
        piinkkLoader.addQuadruple(['print', impre])
        print(f'\t\t\tprint\t{impre}')

    def enterEscri2(self, ctx):
        impre = ctx.getText()[1:-1]
        piinkkLoader.addQuadruple(['print', impre])
        print(f'\t\t\tprint\t{impre}')

    # Exit a parse tree produced by PiinkkParser#escri.
    def exitEscri2(self, ctx):
        pass


# Enter a parse tree produced by PiinkkParser#lectura0.
    def enterLecturaInt0(self, ctx):
        leido = ctx.getText().split('(')[1][:-2]
        print(leido)
        piinkkLoader.addQuadruple(['read', leido])
        print(f'\t\t\tread\t{leido}')
        piinkkLoader.variableCheck(leido)
        piinkkLoader.symbol_table[piinkkLoader.current_scope]['variables'][leido] = {'type': 'int'}
        piinkkLoader.pendientes.append('cambiar enterLectura a constantes enteras')

    # Exit a parse tree produced by PiinkkParser#lectura0.
    def exitLecturaInt0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#return0.
    def enterReturn0(self, ctx):
        piinkkLoader.clearStacks()

    # Exit a parse tree produced by PiinkkParser#return0.
    def exitReturn0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#fun0.
    def enterFun0(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#fun0.
    def exitFun0(self, ctx):
        piinkkLoader.set_current_scope('global')
        piinkkLoader.pendientes.append('eliminar la variTable de la current_scope')

    # Enter a parse tree produced by PiinkkParser#fun1.
    def enterFun1(self, ctx):
        print('ENTRA A FUNCION')
        piinkkLoader.clearStacks()
        fun_info = ctx.getText().split(':')
        fun_type, fun_name = fun_info[0], fun_info[1].split('(')[0]
        piinkkLoader.functionCheck(fun_name)
        piinkkLoader.symbol_table[fun_name] = {'type': fun_type, 'variables': {}}
        piinkkLoader.set_current_scope(fun_name)

    # Exit a parse tree produced by PiinkkParser#fun1.
    def exitFun1(self, ctx):
        pass

    # Enter a parse tree produced by PiinkkParser#fun2.
    def enterFun2(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#fun2.
    def exitFun2(self, ctx):
        pass

    # Enter a parse tree produced by PiinkkParser#fun3.
    def enterFun3(self, ctx):
        var_info = ctx.getText().split(':')
        var_type, var_info = var_info[0], var_info[1]
        scope = piinkkLoader.current_scope
        #  If the next element is an array
        if '[' in var_info:
            var_name, var_arr_size = var_info.split('[')
            var_arr_size = int(var_arr_size.rstrip(']'))
            piinkkLoader.variableCheck(var_name)
            piinkkLoader.symbol_table[scope]['variables'][var_name] = {'type': var_type, 'size': var_arr_size}
        else:
            var_name = var_info
            piinkkLoader.variableCheck(var_name)
            piinkkLoader.symbol_table[scope]['variables'][var_name] = {'type': var_type}
            

    # Exit a parse tree produced by PiinkkParser#fun3.
    def exitFun3(self, ctx):
        pass

    # Enter a parse tree produced by PiinkkParser#body0.
    def enterBody0(self, ctx):
        piinkkLoader.clearStacks()

    # Exit a parse tree produced by PiinkkParser#body0.
    def exitBody0(self, ctx):
        pass


    # Enter a parse tree produced by PiinkkParser#start.
    def enterStart(self, ctx):
        pass

    # Exit a parse tree produced by PiinkkParser#start.
    def exitStart(self, ctx):
        pass
