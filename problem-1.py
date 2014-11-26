#!/usr/bin/python
# -*- coding: utf-8 -*-

from problem import Problem

class Problem1(Problem):
    def solve(self, n):
        sum = 0

        for i in range(999):
            num = i+1

            if num % 3 == 0 or num % 5 == 0:
                sum += num

        return sum

if __name__ == "__main__":
    Problem1().solve_with_timing(1000)
