import ply.yacc as yacc
from lexer import Lexer
import sys
from ply.lex import LexError

class Parser():
	tokens = Lexer.tokens
	
	
	def __init__(self):
		self._lexer = Lexer()
		self._parser = yacc.yacc(module=self)
		
	def check_string(self, s):
		try:
			res = self._parser.parse(s)
			return res
		except LexError:
			sys.stderr.write('illegal token\n')
			
	def p_cmd(self, p):
		'''cmd : create
		| out'''
		p[0] = p[1]
			
	def p_create(self, p):
		'''create : CREATE VAR ARGS NL'''
		p[0] = {'type': 'create','var': p[2], 'args': p[3]}
		
	def p_out_create_var(self, p):
		'out : CREATEVAR NL'
		p[0] = {'type': 'out', 'var': 'create'}
		
	def p_out_create_join(self, p):
		'out : CREATEJOIN VAR NL'
		p[0] = {'type': 'join', 'var1': 'create', 'var2': p[2]}
		
	def p_out_var(self, p):
		'out : VAR NL'
		p[0] = {'type' : 'out', 'var': p[1]}
		
	def p_out_join(self, p):
		'out : VAR JOIN VAR NL'
		p[0] = {'type': 'join', 'var1': p[1], 'var2': p[3]}
	
	def p_create_err_0(self, p):
		'create : CREATE err_list NL'
		p[0] = {'type': 'err', 'val': p[2]}
		
	def p_create_err_1(self, p):
		'create : CREATE VAR err_list NL'
		p[0] = {'type': 'err', 'val': [p[2], p[3]]}
		
		
	def p_create_err_2(self, p):
		'create : CREATE VAR ARGS err_list NL'
		p[0] = {'type': 'err', 'val': [p[2], p[3], p[4]]}
	
	def p_out_err_4(self, p):
		'out : err_list NL'
		p[0] = {'type': 'err', 'val': p[1]}
	
	def p_out_err_2(self, p):
		'out : VAR err_list NL'
		p[0] = {'type': 'err', 'val': [p[1], p[2]]}
	
	
	def p_out_err_1(self, p):
		'out : VAR JOIN err_list NL'
		p[0] = {'type': 'err', 'val': [p[1], p[2], p[3]]}
	
	def p_out_err_0(self, p):
		'out : VAR JOIN VAR err_list NL'
		p[0] = {'type': 'err', 'val': [p[1], p[2], p[3], p[4]]}
	
	def p_err_list_3(self, p):
		'err_list : err_list err'
		p[0] = p[1]
		p[0] += p[2]
	
	def p_err_list_2(self, p):
		'err_list : '
		p[0] = ' '
	
	def p_err_list_1(self, p):
		'err_list : err'
		p[0] = p[1]
	
	def p_err(self, p):
		'err : UNKNOWN'
		p[0] = p[1]
		
	def p_error(self, p):
	   	pass
		
			
if __name__ == '__main__':
	parser = Parser()
	for line in sys.stdin:
		print(parser.check_string(line))