import re
import sys
from copy import copy as cp


class EntityRedefiningError(RuntimeError):
    pass


# r_id = r'create [a-zA-Z\._][a-zA-Z0-9\._]*'

# regex = r'(?i)(create [a-zA-Z\._][a-zA-Z0-9\._]*\([a-zA-Z\._][a-zA-Z0-9\._]*(,[a-zA-Z\._][a-zA-Z0-9\._]*)*\))|([a-zA-Z\._][a-zA-Z0-9\._]*( join [a-zA-Z\._][a-zA-Z0-9\._]*)?)'

# regex = r'(?i)(create {id}\({id}(,{id})*\))|({id}( join {id})?)'.format(id=re.r_id)


# regex = r'(?i)(create \D[a-zA-Z0-9\._]*\(\D[a-zA-Z0-9\._]*(,\D[a-zA-Z0-9\._]*)*\))|(\D[a-zA-Z0-9\._]*( join \D[a-zA-Z0-9\._]*)?)'


regex = r'(create [a-zA-Z\._][a-zA-Z0-9\._]*\([a-zA-Z\._][a-zA-Z0-9\._]*(,[a-zA-Z\._][a-zA_Z0-9\._]*)*\))|([a-zA-Z\._][a-zA-Z0-9\._]*( join [a-zA-Z\._][a-zA_Z0-9\._]*)?)'

class Storage:

    _data = {}

    def __init__(self):
        pass

    def _create(self, expr):
        _expr = expr[:-1].split('(')
        entity_name = _expr[0]
        if entity_name in self._data:
            raise EntityRedefiningError
        entity_attrs = _expr[1].split(',')
        self._data[entity_name] = entity_attrs

    def _output(self, name):
        _name = name.split(' join ')
        if len(_name) == 1:
            if name in self._data:
                print(self._data[name])
            else:
                raise AttributeError
        else:
            if not (_name[0] in self._data and _name[1] in self._data):
                raise AttributeError
            ans = []
            set0 = set(self._data[_name[0]])
            set1 = set(self._data[_name[1]])
            intersection = list(set0 & set1)
            for item in intersection:
                ans.append(_name[0]+'.'+item)
                ans.append(_name[1]+'.'+item)
            ans += list(set0 - set1)
            print(ans)

    def analyze(self, expr_):
        if re.match(regex, expr_):
            _expr = expr_.split()
            if _expr[0] == 'create':
                try:
                    self._create(_expr[1])
                    sys.stderr.write('SUCCESS '+expr)
                except EntityRedefiningError:
                    sys.stderr.write('ERROR '+expr)
            else:
                try:
                    self._output(_expr)
                    sys.stderr.write('SUCCESS '+expr)
                except AttributeError:
                    sys.stderr.write('ERROR '+expr)
        else:
            sys.stderr.write('FAIL '+expr)


if __name__ == '__main__':
    storage = Storage()
    while True:
        expr = input()
        print(re.fullmatch(regex, expr))
        # if expr is not None:
        #    storage.analyze(expr)
