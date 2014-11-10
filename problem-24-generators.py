#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

class Problem24():
    def gen_perms(self, input):
        input = tuple(input)

        for n in xrange(len(input)):
            if len(input) > 2:
                for i in self.gen_perms(input[:n] + input[n+1:]):
                    yield (input[n],) + i
            else:
                yield input if n == 0 else (input[n],) + input[:n] + input[n+1:]

    def solve(self, n):
        index = 0
        for n in self.gen_perms(range(n)):
            if index == 999999:
                return "".join("{0}".format(i) for i in n)
                break
            index += 1

if __name__ == "__main__":
    problem = Problem24()

    start = time.time()
    print problem.solve(10)
    end = time.time()

    print "Took {0} seconds".format(end - start)
