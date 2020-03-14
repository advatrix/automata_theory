import Detector
import sys
from copy import copy
import time


class EntityRedefiningError(Exception):
    pass


class Storage:

    def __init__(self):
        self._data = {}

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
                ans.append(key1 + '.' + item)
                ans.append(key2 + '.' + item)
            ans += list(set0 - set1)
            ans += list(set1 - set0)
            print(ans)


    def analyze(self, expr_):
        detector = Detector.Detector()
        res = detector.checkstring(expr_)
        if res[0] or res[1] or res[2]:
            _expr = expr_.split()
            if res[0]:
                try:
                    self._create(_expr[1])
                    sys.stderr.write('SUCCESS ' + expr_ + '\n')
                except EntityRedefiningError:
                    sys.stderr.write('REDEFINING ERROR ' + expr_ + '\n')
            else:
                try:
                    self._output(_expr)
                    sys.stderr.write('SUCCESS ' + expr_ + '\n')
                except AttributeError:
                    sys.stderr.write('ATTRIBUTE ERROR ' + expr_ + '\n')
        else:
            sys.stderr.write('WRONG COMMAND ' + expr_ + '\n')


if __name__ == '__main__':
    storage = Storage()
    start = time.time()
    for expr in sys.stdin:
        storage.analyze(expr[:-1])
    end = time.time()
    with open('time.txt', 'w+') as f:
        f.write(str(end-start))
