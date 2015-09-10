#!/usr/bin/python
# -*- coding: utf-8 -*-

from problem import Problem


class Problem4(Problem):
    def solve(self, n):
        biggest = 0
        r = range(2, pow(10, n)) 

        for i in r: 
            for j in r:
                product = i * j

                if str(product) == str(product)[::-1] and product > biggest:
                    biggest = product

        return biggest

if __name__ == "__main__":
    Problem4().cli_interface(3)
