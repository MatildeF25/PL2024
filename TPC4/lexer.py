import ply.lex as lex

# Lista de nomes de tokens
tokens = (
    'SELECT',
    'VARIABLE',
    'FROM',
    'WHERE',
    'COMMA',
    'NUMBER',
    'EQUALS',
    'GREATER_THAN',
    'LESS_THAN',
    'GREATER_THAN_EQUALS',
    'LESS_THAN_EQUALS'
)


# Regular expression rules for simple tokens
t_SELECT = r'SELECT'
t_FROM = r'FROM'
t_WHERE = r'WHERE'
t_VARIABLE = r'id|nome|salario|empregados|salario'
t_COMMA = r','
t_NUMBER = r'\d+'
t_EQUALS = r'\='
t_GREATER_THAN = r'\>'
t_LESS_THAN = r'\<'
t_GREATER_THAN_EQUALS = r'\>\='
t_LESS_THAN_EQUALS = r'\<\='


# ignorar caracteres em branco
t_ignore = " \t"

# Regra para tratar quebra de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Regra para tratar erros
def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir o lexer
lexer = lex.lex()

# Testa o lexer
data = '''
SELECT id, nome, salario FROM empregados WHERE salario => 1000
'''

# Testa o lexer
lexer.input(data)


# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

