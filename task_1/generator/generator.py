import random
import exrex
import string


class Generator:

    def __init__(self, regex, n, target_file='out.txt', accuracy=0.8):
        self._n = n
        self._regex = regex
        self._accuracy = accuracy
        self._target_file = target_file

    def generate(self):
        ret = []
        generator = exrex.generate(self._regex, self._n)
        for i in range(self._n):
            tmp_string = generator.__next__()
            if random.random() > self._accuracy:
                err_string = self.spoil(tmp_string)
                ret.append(err_string)
            else:
                ret.append(tmp_string)
        with open(target_file) as f:
            f.writelines(ret)

    @staticmethod
    def spoil(str_):
        s = list(str_)
        n_iterations = random.randint(1, len(s))
        for i in range(n_iterations):
            idx = random.randint(0, len(s) + 1)
            if idx == len(s):
                s = random.choice(string.printable) + s
            elif idx == len(s) + 1:
                s += random.choice(string.printable)
            else:
                s[idx] = random.choice(string.printable)
        return "".join(s)


if __name__ == '__main__':
    regex, n, target_file, accuracy = input()
    n = int(n)
    accuracy = float(accuracy)
    random.seed()
    generator = Generator(regex, n, target_file, accuracy)
    generator.generate()

