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
        return [x for x in range(2, int(math.ceil(math.sqrt(n))))
                if (n / float(x)) % 1.0 == 0.0and self.is_prime(x)][-1]

if __name__ == "__main__":
    Problem3().cli_interface(600851475143)
