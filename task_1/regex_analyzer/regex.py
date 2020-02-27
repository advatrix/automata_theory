import re
import sys
from copy import copy


class EntityRedefiningError(RuntimeError):
    pass


regex = r'(create [a-zA-Z\._][a-zA-Z0-9\._]*\([a-zA-Z\._][a-zA-Z0-9\._]*(,[a-zA-Z\._][a-zA_Z0-9\._]*)*\))|([a-zA-Z\._][a-zA-Z0-9\._]*( join [a-zA-Z\._][a-zA_Z0-9\._]*)?)'


class Storage:

    _data = {}

    def __init__(self):
        pass

    def _create(self, expr):
        _expr = expr[:-1].split('(')
        entity_name = _expr[0]
        if entity_name in self._data.keys():
            raise EntityRedefiningError
        entity_attrs = _expr[1].split(',')
        self._data[entity_name] = entity_attrs

    def _output(self, name):
        _name = copy(name)
        if len(_name) == 1:
            key = ''.join(_name)
            if key in self._data.keys():
                print(self._data[key])
            else:
                raise AttributeError
        else:
            if not (_name[0] in self._data.keys() and _name[2] in self._data.keys()):
                raise AttributeError
            ans = []
            key1 = ''.join(_name[0])
            key2 = ''.join(_name[2])
            set0 = set(self._data[key1])
            set1 = set(self._data[key2])
            intersection = list(set0 & set1)
            for item in intersection:
                ans.append(key1+'.'+item)
                ans.append(key2+'.'+item)
            ans += list(set0 - set1)
            ans += list(set1 - set0)
            print(ans)

    def analyze(self, expr_):
        if re.fullmatch(regex, expr_):
            _expr = expr_.split()
            if _expr[0] == 'create' and len(_expr) > 1 and '(' in _expr[1]:
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
        if expr is not None:
            storage.analyze(expr)
