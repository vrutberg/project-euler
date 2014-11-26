#!/usr/bin/python
# -*- coding: utf-8 -*-

from problem import Problem

class Problem24(Problem):
    def gen_perms(self, input):
        input = tuple(input)
        perms = []

        for n in range(len(input)):
            if len(input) > 2:
                for i in self.gen_perms(input[:n] + input[n+1:]):
                    perms.append((input[n],) + i)
            else:
                perms.append(input if n == 0 else (input[n],) + input[:n] + input[n+1:])

        return tuple(perms)

    def solve(self, n):
        index = 0
        for n in self.gen_perms(range(n)):
            if index == 999999:
                return "".join("{0}".format(i) for i in n)
                break
            index += 1

if __name__ == "__main__":
    Problem24().solve_with_timing(10)
