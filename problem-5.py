#!/usr/bin/python
# -*- coding: utf-8 -*-

from problem import Problem


class Problem5(Problem):
    def solve(self, input_value):
        numbers = list(range(1, input_value + 1))
        numbers.reverse()

        n = numbers[0]

        while True:
            divisible = True

            for x in numbers:
                if n % x != 0:
                    divisible = False
                    break

            if divisible:
                break

            n += numbers[0]

        return n

if __name__ == "__main__":
    Problem5().cli_interface(20)
