#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

class Problem():
    def solve_with_timing(self, *args):
        start = time.time()

        print self.solve(*args)

        end = time.time()

        print "Took {0} seconds".format(end - start)
