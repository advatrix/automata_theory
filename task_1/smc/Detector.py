import Detector_sm


class Detector:
    def __init__(self):
        self._fsm = Detector_sm.Detector_sm(self)
        self._create_flag = False
        self._join_flag = False
		self._set_out_flag = False
        self._var = []
        self._other_var = []
        self._args = []
		self._arg = []
		self._cmd = []
		self._counter = 0
		self._join = []

    def set_create_flag(self):
        self._create_flag = True

    def reset_create_flag(self):
        self._create_flag = False

    def set_join_flag(self):
        self._join_flag = True

    def reset_join_flag(self):
        self._join_flag = False
		
    def set_out_flag(self):
		self._out_flag = True
		
	def reset_out_flag(self):
		self._out_flag = False

	def inc_counter(self):
		self._counter += 1
		
	def cmd_update(self, lt):
		self._cmd.append(lt)
		
	def cmd_is_create(self):
		return ''.join(self._cmd) == 'create'
	
	def counter(self):
		return self._counter
	
	def reset_counter(self):
		self._counter = 0
		
	def var_update(self, lt):
		self._var.append(lt)
		
	def var_is_join(self):
		return ''.join(self._var) == 'join'
	
	def arg_update(self, lt):
		self._arg.append(lt)
	
	def arg_append(self):
		self._args.append(self._arg)
		self._arg = []
		
	def args(self):
		return self._args
	
	def join_update(self, lt):
		self._join.append(lt)
		
	def join_is_join(self):
		return ''.join(self._join) == 'join'
	
	def other_var_update(self, lt):
		self._other_var.append(lt)
						  
	
						  
						  
	
	