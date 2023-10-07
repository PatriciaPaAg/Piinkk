grammar piinkk;

fileconfig0: PROGRAM PROGRAMID vars0* fun0*  body0;

type0: INT | FLOAT | CHAR;
array0: ID '[' NUMBER ']';

vars0: VARS (type0 ((ID | array0) ','?)+ )+';' ;
fun0: FUNCTION;
body0: MAIN;
start : 'hola mundo' ;


PROGRAM: 'Program';
PROGRAMID: [A-Z][a-zA-Z0-9_]*?;
MAIN: 'main';
COMMENT: '%%'(.)*?;
VARS: 'VARS';
ID: [a-z][a-zA-Z0-9_]*?;
FUNCTION:'function';
INT: 'int';
FLOAT: 'float';
NUMBER: [0-9]+;
CHAR: 'char';
VOID: 'void';
RETURN: 'return';
READ: 'read';
WRITE: 'write';
IF: 'if';
THEN: 'then';
ELSE: 'else';
WHILE: 'while';	
TO: 'to';
MEDIA: 'Media';
MODA: 'Moda';
VARIANZA: 'Varianza';
REGRESIONSIMPLE: 'RegresionSimple';
PLOTXY: 'PlotXY';
MEDIANA: 'Mediana';
DESVIACIONESTANDAR: 'DesviacionEstandar';
RANGO: 'Rango';
COEFICIENTEVARIACION: 'CoeficienteVariacion';
WS: [\t\n\r]+;