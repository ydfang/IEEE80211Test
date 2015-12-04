# -*- coding: utf-8 -*-

'''Fibonacc using list

Implement Fib
'''

from decorators import trace

@trace
def fib(n):
    return (n in (0, 1) and [n] or [fib(n - 1) + fib(n - 2)])[0]


if __name__ == '__main__':
    import sys
    print(fib(10))
