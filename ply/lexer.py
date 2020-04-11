import ply.lex as lex
import re
import sys

class Lexer():
	states = (
		('create', 'exclusive'), 
		('out', 'exclusive'),
	)
	
	tokens = (
		'CREATE', 'VAR', 'ARGS', 'JOIN', 'CREATEVAR', 'CREATEJOIN', 'UNKNOWN', 'NL'
	)
	
	t_ignore = ''
	t_create_ignore = ''
	t_out_ignore = ''
	
	def __init__(self):
		self.lexer = lex.lex(module=self)
	
	def input(self, data):
		return self.lexer.input(data)
	
	def t_CREATEJOIN(self, t):
		r'(create\sjoin\s)'
		t.lexer.begin('out')
		return t
	
	def t_CREATE(self, t):
		r'(create\s)'
		t.lexer.begin('create')
		return t
	
	def t_CREATEVAR(self, t):
		r'create'
		t.lexer.begin('out')
		return t
	
	def t_VAR(self, t):
		r'[a-zA-Z\.\_][a-zA-Z0-9\.\_]*'
		t.lexer.begin('out')
		return t
	
	def t_ANY_NL(self, t):
		r'\n'
		t.lexer.begin('INITIAL')
		return t
	
	def t_newline(self, t):
		r'\n+'
		t.lexer.lineno += t.value.count('\n')
		t.lexer.begin('INITIAL')
		return t
		
	def t_create_VAR(self, t):
		r'[a-zA-Z\.\_][a-zA-Z0-9\.\_]*'
		return t
	
	def t_create_ARGS(self, t):
		r'\([a-zA-Z\.\_][a-zA-Z0-9\.\_]*(,[a-zA-Z\.\_][a-zA-Z0-9\.\_]*)*\)'
		return t
	
	def t_create_newline(self, t):
		r'\n+'
		t.lexer.lineno += t.value.count('\n')
		t.lexer.begin('INITIAL')
		return t
		
	def t_out_JOIN(self, t):
		r'(\sjoin\s)'
		return t
	
	def t_out_VAR(self, t):
		r'[a-zA-Z\.\_][a-zA-Z0-9\.\_]*'
		return t
	
	def t_out_newline(self, t):
		r'\n+'
		t.lexer.lineno += t.value.count('\n')
		t.lexer.begin('INITIAL')
		return t	
	
	def t_ANY_UNKNOWN(self, t):
		r'.+'
		return t

	def t_ANY_error(self, t):
		sys.stderr.write("Illegal character '%s'\n" % t.value[0])
		t.lexer.skip(1)
		t.lexer.begin('INITIAL')
		
	'''	
	def t_out_error(self, t):
		sys.stderr.write("Illegal character '%s'\n" % t.value[0])
		t.lexer.begin('INITIAL')
		
	def t_create_error(self, t):
		sys.stderr.write("Illegal character '%s'\n" % t.value[0])
		t.lexer.begin('INITIAL')
		'''
	
	def token(self):
		return self.lexer.token()
	
		
if __name__ == '__main__':
	lexer = Lexer()
	lexer.input(input())
	for tok in lexer.lexer:
		print(tok)
	
		