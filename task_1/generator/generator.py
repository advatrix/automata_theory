#!/usr/bin/env python

import random
import exrex
import string


class Generator:

    def __init__(self, regex, n, target_file='out.txt', accuracy=0.8, length_limit=20):
        self._n = n
        self._regex = regex
        self._accuracy = accuracy
        self._target_file = target_file
        self._length_limit = length_limit

    def generate(self):
        ret = []
        # generator = exrex.generate(self._regex, self._n)
        for i in range(self._n):
            # tmp_string = generator.__next__()
            tmp_string = exrex.getone(self._regex, self._length_limit)
            if random.random() > self._accuracy:
                err_string = self.spoil(tmp_string)
                ret.append(err_string+'\n')
            else:
                ret.append(tmp_string+'\n')
        with open(target_file, 'w+') as f:
            f.writelines(ret)

    @staticmethod
    def spoil(str_):
        s = list(str_)
        if len(s):
            n_iterations = random.randint(1, len(s))
            for i in range(n_iterations):
                idx = random.randint(0, 2 * len(s) + 1)
                if idx == len(s):
                    s.insert(0, random.choice(string.printable))
                elif idx == len(s) + 1:
                    s.append(random.choice(string.printable))
                elif idx < len(s):
                    s[idx] = random.choice(string.printable)
                else:
                    del s[idx - 2 - len(s)]
        return "".join(s)


if __name__ == '__main__':
    regex = input()
    n = input()
    target_file = input()
    accuracy = input()
    n = int(n)
    accuracy = float(accuracy)
    random.seed()
    generator = Generator(regex, n, target_file, accuracy)
    generator.generate()

