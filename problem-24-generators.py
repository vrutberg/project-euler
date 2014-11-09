#!/usr/bin/python
# -*- coding: utf-8 -*-

class Problem24():

    def gen_perms(self, input):
        input = tuple(input)

        for n in input:
            tmp = input if input[0] == n else (n,) + tuple(x for x in input if x != n)

            if len(tmp) > 2:
                for i in self.gen_perms(tmp[1:]):
                    yield (n,) + i
            else:
                yield tmp

    def solve(self, n):
        index = 0
        for n in self.gen_perms(range(n)):
            if index == 999999:
                return "".join("{0}".format(i) for i in n)
                break
            index += 1

if __name__ == "__main__":
    problem = Problem24()
    print problem.solve(10)
