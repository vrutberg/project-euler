#!/usr/bin/python
# -*- coding: utf-8 -*-

from problem import Problem


class Problem2(Problem):
    def solve(self, n):
        result = 0

        n1 = 1
        n2 = 1

        while True:
            tmp = n1 + n2

            if tmp >= n:
                break

            if tmp % 2 == 0:
                result += tmp

            n1 = n2
            n2 = tmp

        return result

if __name__ == "__main__":
    Problem2().cli_interface(4000000)
