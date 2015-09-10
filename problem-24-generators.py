#!/usr/bin/python
# -*- coding: utf-8 -*-

from problem import Problem


class Problem24(Problem):
    def gen_perms(self, input_value):
        input_value = tuple(input_value)

        for n in range(len(input_value)):
            if len(input_value) > 2:
                for i in self.gen_perms(input_value[:n] + input_value[n+1:]):
                    yield (input_value[n],) + i
            else:
                yield input_value if n == 0 else (input_value[n],) + input_value[:n] + input_value[n+1:]

    def solve(self, n):
        index = 0
        for n in self.gen_perms(range(n)):
            if index == 999999:
                return "".join("{0}".format(i) for i in n)
            index += 1

if __name__ == "__main__":
    Problem24().cli_interface(10)
