"""
Problem Statement Found At: https://www.hackerrank.com/challenges/30-recursion/problem
"""


def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1
