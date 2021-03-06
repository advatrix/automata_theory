import Detector_sm


class Detector:
    def __init__(self):
        self._fsm = Detector_sm.Detector_sm(self)
        self._create_flag = False
        self._join_flag = False
        self._out_flag = False
        self._var = []
        self._other_var = []
        self._args = []
        self._arg = []
        self._cmd = []
        self._counter = 0
        self._join = []
        self._acceptable = True

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
        
    def unacceptable(self):
        self._acceptable = False

    def checkstring(self, string):
        self._fsm.enterStartState()
        for c in string:
            if not self._acceptable:
                return False, False, False
            if c.isdigit():
                self._fsm.digit(c)
            elif c.isalpha() or c == '.' or c == '_':
                self._fsm.letter(c)
            elif c == ' ':
                self._fsm.space()
            elif c == ')':
                self._fsm.cbracket()
            elif c == '(':
                self._fsm.obracket()
            elif c == ',':
                self._fsm.comma()
            else:
                self._fsm.Default()
        self._fsm.EOS()
        return self._create_flag, self._out_flag, self._join_flag           
