import ply.lex as lex

# Lista de nomes de tokens
tokens = (
    'SELECT',
    'ID',
    'NOME',
    'SALARIO',
    'FROM',
    'EMPREGADOS',
    'WHERE',
    'COMMA',
    'NUMBER',
    'OPERATOR',
)


# Regular expression rules for simple tokens
t_SELECT = r'SELECT'
t_ID = r'id'
t_NOME = r'nome'
t_SALARIO = r'salario'
t_FROM = r'FROM'
t_EMPREGADOS = r'empregados'
t_WHERE = r'WHERE'
t_COMMA = r','
t_NUMBER = r'\d+'
t_OPERATOR = r'[><=]+'

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
SELECT id, nome, salario FROM empregados WHERE salario >= 1000
'''

# Testa o lexer
lexer.input(data)


# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

