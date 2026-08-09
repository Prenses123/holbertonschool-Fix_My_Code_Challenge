#!/usr/bin/python3
"""
FizzBuzz evaluation
"""
import sys

def fizzbuzz(n):
    if n < 1:
        return

    tmp_nos = []
    for i in range(1, n + 1):
        # Check for combined condition FIRST
        if (i % 3 == 0) and (i % 5 == 0):
            tmp_nos.append("FizzBuzz")
        elif i % 3 == 0:
            tmp_nos.append("Fizz")
        elif i % 5 == 0:
            tmp_nos.append("Buzz")
        else:
            tmp_nos.append(str(i))
    print(" ".join(tmp_nos))

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        fizzbuzz(100)
    else:
        fizzbuzz(int(sys.argv[1]))
