#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import itertools

class Problem24():

    def solve(self, n):
        index = 0
        for n in itertools.permutations(range(n)):
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
