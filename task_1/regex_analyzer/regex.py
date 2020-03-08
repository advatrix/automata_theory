import re
import sys
from copy import copy


class EntityRedefiningError(RuntimeError):
    pass


# regex = r'(create [a-zA-Z\._][a-zA-Z0-9\._]*\([a-zA-Z\._][a-zA-Z0-9\._]*(,[a-zA-Z\._][a-zA_Z0-9\._]*)*\))|([a-zA-Z\._][a-zA-Z0-9\._]*( join [a-zA-Z\._][a-zA_Z0-9\._]*)?)'

regex = re.compile(r'(create (?P<var>[a-zA-Z._][a-zA-Z0-9._]*)'
                   r'(?P<args>\([a-zA-Z._][a-zA-Z0-9\._]*(,[a-zA-Z\._][a-zA-Z0-9\._]*)*\)))|'
                   r'((?P<var1>[a-zA-Z._][a-zA-Z0-9._]*)( join (?P<var2>[a-zA-Z._][a-zA-Z0-9._]*))?)', re.IGNORECASE
                   )


class Storage:

    _data = {}

    def __init__(self):
        pass

    def __create(self, var, args):
        if var in self._data.keys():
            raise EntityRedefiningError
        attrs = args[1:-1].split(',')
        self._data[var] = attrs

    def __output(self, var1, var2):
        if var1 in self._data.keys():
            if var2:
                if var2 in self._data.keys():
                    ans = []
                    set1 = set(self._data[var1])
                    set2 = set(self._data[var2])
                    intersection = list(set1 & set2)
                    for item in intersection:
                        ans.append(var1 + '.' + item)
                        ans.append(var2 + '.' + item)
                    ans += list(set1 - set2)
                    ans += list(set2 - set1)
                    return ans
                else:
                    raise AttributeError
            else:
                return self._data[var1]
        else:
            raise AttributeError

    def analyze(self, expr_):
        if re.fullmatch(regex, expr_):
            res_dict = re.search(regex, expr_).groupdict()
            if res_dict['var']:
                try:
                    self.__create(res_dict['var'], res_dict['args'])
                    sys.stderr.write('SUCCESS '+expr+'\n')
                except EntityRedefiningError:
                    sys.stderr.write('REDEFINING ERROR '+expr+'\n')
            elif res_dict['var1']:
                try:
                    print(self.__output(res_dict['var1'], res_dict['var2']))
                    sys.stderr.write('SUCCESS '+expr+'\n')
                except AttributeError:
                    sys.stderr.write('ATTRIBUTE ERROR ' + expr + '\n')
            else:
                sys.stderr.write('UNKNOWN ERROR ' + expr + '\n')
        else:
            sys.stderr.write('WRONG COMMAND ' + expr + '\n')


if __name__ == '__main__':
    storage = Storage()
    while True:
        expr = input()
        if expr is not None:
            storage.analyze(expr)
