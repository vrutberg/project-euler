#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools

from problem import Problem

class Problem24(Problem):
    def solve(self, n):
        index = 0
        for n in itertools.permutations(range(n)):
            if index == 999999:
                return "".join("{0}".format(i) for i in n)
                break
            index += 1

if __name__ == "__main__":
    Problem24().cli_interface(10)
