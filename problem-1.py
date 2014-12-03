#!/usr/bin/python
# -*- coding: utf-8 -*-

from problem import Problem

class Problem1(Problem):
    def solve(self, n):
        result = 0

        result += sum(range(3, n, 3)) + sum(range(5, n, 5))
        result -= sum(range(15, n, 15))

        return result

if __name__ == "__main__":
    Problem1().cli_interface(1000)
