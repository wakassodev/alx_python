#!/usr/bin/python3
def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence = fib_sequence + [next_number]
    return fib_sequence[:n]