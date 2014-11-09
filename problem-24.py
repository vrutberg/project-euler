#!/usr/bin/python
# -*- coding: utf-8 -*-

class Problem24():

    def gen_perms(self, input):
        input = tuple(input)
        perms = []

        for n in input:
            tmp = input if input[0] == n else (n,) + tuple(x for x in input if x != n)

            if len(tmp) > 2:
                for i in self.gen_perms(tmp[1:]):
                    perms.append((n,) + i)
            else:
                perms.append(tmp)

        return tuple(perms)

    def solve(self, n):
        return "".join("{0}".format(n) for n in self.gen_perms(range(n))[999999])

if __name__ == "__main__":
    problem = Problem24()
    print problem.solve(10)