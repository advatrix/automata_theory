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
			
	def join(self, var1 : str, var2 : str) -> list[str]:
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
			print(ans)
		else:
			raise AttributeError
			
class Analyzer():
	def __init__(self):
		self._parser = Parser()
		
	def analyze(self, expr, st):
		res = self._parser.check_string(expr)
		if res is None:
			sys.stderr.write('FAIL ' + expr)
			return
		if res['type'] == 'create':
			try:
				st.create(res['var'], res['args'][1:-1].split(','))
				sys.stderr.write('SUCCESS ' + expr)
			except EntityRedefiningError:
				sys.stderr.write('REDEFINING ERROR ' + expr)
		elif res['type'] == 'out':
			try:
				st.out(res['var'])
				sys.stderr.write('SUCCESS ' + expr)
			except AttributeError:
				sys.stderr.write('ATTRIBUTE ERROR ' + expr)
		elif res['type'] == 'join':
			try:
				st.join(res['var1'], res['var2'])
				sys.stderr.write('SUCCESS ' + expr)
			except AttributeError:
				sys.stderr.write('ATTRIBURE ERROR ' + expr)
		elif res['type'] == 'err':
			sys.stderr.write('FAIL ' + expr)
				
if __name__ == '__main__':
	storage = Storage()
	analyzer = Analyzer()
	start = time.time()
	for expr in sys.stdin:
		analyzer.analyze(expr, storage)
	end = time.time()
	with open('time.txt', 'w+') as f:
		f.write(str(end-start))
			
			