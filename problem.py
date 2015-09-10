#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import argparse


class Problem(object):
    def solve_with_timing(self, iterations, *args):
        if iterations is None:
            iterations = 1

        start = time.time()
        result = 0

        for i in range(iterations):
            result = self.solve(*args)

        end = time.time()

        print("Input: {0}".format(*args))
        print("Result: {0}".format(result))
        print("{0} iteration(s) took {1} seconds".format(iterations, end - start))

    def cli_interface(self, input_value=None):
        parser = argparse.ArgumentParser(description="Solve a Project Euler problem.")

        parser.add_argument("input", nargs="?", default=input_value, type=int, help="input for the problem")
        parser.add_argument("-n", default=1, type=int, help="number of iterations")

        args = parser.parse_args()

        self.solve_with_timing(args.n, args.input)

    def solve(self, param):
        pass
