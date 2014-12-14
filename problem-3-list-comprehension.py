#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

from problem import Problem

class Problem3(Problem):

    def isPrime(self, n):
        for i in xrange(2, n/2):
            if n % i == 0:
                return False

        return True

    def solve(self, n):
        return [x for x in xrange(2, int(math.ceil(math.sqrt(n)))) if (n / float(x)) % 1.0 == 0.0 and self.isPrime(x)][-1]

if __name__ == "__main__":
    Problem3().cli_interface(600851475143)
