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
        r = -1

        for i in xrange(2, int(math.ceil(math.sqrt(n)))):
            if (n / float(i)) % 1.0 == 0.0 and self.isPrime(i):
                r = i

        return r

if __name__ == "__main__":
    Problem3().cli_interface(600851475143)
