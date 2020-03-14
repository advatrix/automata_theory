from parser import Parser
import sys
import time

class EntityRedefiningError(Exception):
	pass

class Storage():
	def __init__(self):
		self._data = {}
		
	def create(self, var, args):
		if var not in self._data.keys():
			self._data[var] = args
		else:
			raise EntityRedefiningError
	
	def out(self, var):
		if var in self._data.keys():
			print(self._data[var])
		else:
			raise AttributeError
			
	def join(self, var1, var2):
		if var1 in self._data.keys() and var2 in self._data.keys():
			ans = []
			set1 = set(self._data[var1])
			set2 = set(self._data[var2])
			intersection = list(set1 & set2)
			for item in intersection:
				ans.append(var1 + '.' + item)
				ans.append(var2 + '.' + item)
			ans += list(set1 - set2)
			ans += list(set2 - set1)
		else:
			raise AttributeError
			
class Analyzer():
	def __init__(self):
		self._parser = Parser()
		
	def analyze(self, expr, st):
		res = self._parser.check_string(expr)
		if res['type'] == 'create':
			try:
				st.create(res['var'], res['args'][1:-1].split(','))
				sys.stderr.write('SUCCESS ' + expr + '\n')
			except EntityRedefiningError:
				sys.sterr.write('REDEFINING ERROR
				
		elif res['type'] == 'out':
			st.out(res['var'])
		elif res['type'] == 'join':
			
			