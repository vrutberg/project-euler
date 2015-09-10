#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

from problem import Problem


class Problem3(Problem):

    @staticmethod
    def is_prime(n):
        for i in range(2, int(n/2)):
            if n % i == 0:
                return False

        return True

    def solve(self, n):
        r = -1

        for i in range(2, int(math.ceil(math.sqrt(n)))):
            if (n / float(i)) % 1.0 == 0.0 and self.is_prime(i):
                r = i

        return r

if __name__ == "__main__":
    Problem3().cli_interface(600851475143)
