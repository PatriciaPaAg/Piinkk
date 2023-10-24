grammar Piinkk;

prog: PROGRAM PROGRAMID ';' vars0 fun0* body0;
type0: INT | FLOAT | CHAR;
array0: ID '[' NUMBER ']';

if0: IF '(' expresion0 ')' bloque0 (ELSE bloque0)?;
while0: WHILE '(' expresion0 ')' DO bloque0;
for0: FOR ID '=' exp0 TO exp0 DO bloque0;

var0: ID | array0 | NUMBER | FLOAT_NUMBER;
vars0: VARS (type0 var0 (',' var0)* ';')+;

expresion0: exp0 (('==' | '>' | '<' | '!=' | '>=' | '<=') exp0)?;

exp0: termino0 (('+' | '-') exp0)?;

termino0: factor0 (('*' | '/') termino0)?;

factor0: ('(' expresion0 ')') | var0;

bloque0: '{' estatuto0* '}';
estatuto0: asignacion0
            | if0
            | while0
            | for0
            | escritura0
            | return0;
            
asignacion0: ID '=' expresion0 ';';

escri: expresion0 | 'cte.string';
escritura0: WRITE '(' escri (',' escri)* ')' ';';
return0: RETURN '(' exp0 ')' ';' ;

fun0: FUNCTION type0 ID '(' (type0 var0 (',' type0 var0)* )? ')' vars0? bloque0;
body0: MAIN '('')' bloque0;
start : 'hola mundo' ;


PROGRAM: 'Program';
MAIN: 'main';
COMMENT: '%%'(.)*?;
VARS: 'VARS';
FUNCTION:'function';
INT: 'int';
FLOAT: 'float';
CHAR: 'char';
VOID: 'void';
RETURN: 'return';
READ: 'read';
WRITE: 'write';
IF: 'if';
THEN: 'then';
ELSE: 'else';
WHILE: 'while';	
DO: 'do';
FOR: 'FOR';
TO: 'to';
MEDIA: 'Media';
MODA: 'Moda';
VARIANZA: 'Varianza';
REGRESION_SIMPLE: 'RegresionSimple';
PLOTXY: 'PlotXY';
MEDIANA: 'Mediana';
DESVIACION_ESTANDAR: 'DesviacionEstandar';
RANGO: 'Rango';
COEFICIENTE_VARIACION: 'CoeficienteVariacion';
WS: [ \t\n\r]+ -> skip;
NUMBER: [0-9]+;
FLOAT_NUMBER: NUMBER '.' [0-9]+;
PROGRAMID: [A-Z][a-zA-Z0-9_]*;
ID: [a-z][a-zA-Z0-9_]*;