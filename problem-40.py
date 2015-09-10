#!/usr/bin/python
# -*- coding: utf-8 -*-

from problem import Problem


class Problem40(Problem):
    @staticmethod
    def get_index(n):
        return int("".join([str(x) for x in range(1, n+1)])[n-1])

    def solve(self, numbers):
        product = 1

        for n in numbers:
            product *= self.get_index(n)

        return product

if __name__ == "__main__":
    Problem40().cli_interface([1, 10, 100, 1000, 10000, 100000, 1000000])
