#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from decimal import *
from problem import Problem

class Problem26(Problem):
    def solve(self, n):
        result = { 'index': 0, 'cycle': '' }
        results = {}

        for x in range(2, n+1):
            getcontext().prec = x * 2

            searchResult = re.findall('(\\d+)\\1', str(Decimal(1.0)/Decimal(x)))

            if len(searchResult) > 0:
                results[x] = self.longest_match(searchResult)

        for x in results:
            if len(results[x]) > len(result['cycle']):
                result["index"] = x
                result["cycle"] = results[x] 

        return result

    def longest_match(self, array):
        if len(array) == 0:
            return None
        elif len(array) == 1:
            return self.normalize_match(array[0])

        result = ""

        for x in array: 
            validatedMatch = self.normalize_match(x)
            if len(validatedMatch) > len(result):
                result = validatedMatch

        return result

    def normalize_match(self, potentialMatch):
        normalized = re.findall("^(\\d+?)\\1+$", potentialMatch)

        if len(normalized) == 1:
            return normalized[0]
        else:
            return potentialMatch

if __name__ == "__main__":
    Problem26().cli_interface(1000)
