#!/usr/bin/env python
"""Implements math functions without using operators,
except for '+' and '-'.
"""

__author__ = "Jordan Kubista"


def add(x, y):
    """Add two integers."""
    sum_equals = x + y
    return sum_equals


def multiply(x, y):
    """Multiply x with y using the add() function above."""
    product = 0
    for i in range(1, abs(y)+1):

        product = add(product, abs(x))

    if x > 0 and y > 0 or x < 0 and y < 0:
        return product
    else:
        return -product


def power(x, n):
    """Raise x to power n, where n >= 0, using the functions above."""
    power_of = 1

    for i in range(1, n + 1):
        power_of = multiply(power_of, x)

    return power_of


def factorial(x):
    """Compute the factorial of x, where x > 0, using the functions above."""
    factorial_of = x

    if x < 2:
        return 1
    else:
        for i in range(x - 1, 0, -1):

            factorial_of = multiply(factorial_of, i)

    return factorial_of


def fibonacci(n):
    """Compute the nth term of fibonacci sequence using the functions above."""
    fib_seq = [0, 1]

    for i in range(n):
        fib_seq.append(add(fib_seq[-1], fib_seq[-2]))
    print(fib_seq)
    return fib_seq[n]


print(fibonacci(11))

if __name__ == '__main__':
    # your code to call functions above
    pass
