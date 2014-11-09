#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools

class Problem24():

    def solve(self, n):
        return "".join("{0}".format(n) for n in list(itertools.permutations(range(n)))[999999])

if __name__ == "__main__":
    problem = Problem24()
    print problem.solve(10)
