#!/usr/bin/python
# -*- coding: utf-8 -*-

from problem import Problem

class Problem5(Problem):
    def solve(self, numbers):
        n = numbers[-1]
        numbers.reverse()

        while True:
            divisible = True

            for x in numbers:
                if n % x != 0:
                    divisible = False
                    break

            if divisible:
                break

            n += 2

        return n

if __name__ == "__main__":
    Problem5().cli_interface(range(1, 21))
