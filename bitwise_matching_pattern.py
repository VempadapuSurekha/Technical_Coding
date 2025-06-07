"""
Problem 4: Bitwise Matching Pattern

Given an integer n, return the next larger integer with the same number of 1s in binary.
"""

def next_higher_with_same_ones(n):
    c = n
    c0 = c1 = 0

    while ((c & 1) == 0) and (c != 0):
        c0 += 1
        c >>= 1

    while (c & 1) == 1:
        c1 += 1
        c >>= 1

    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1

    p = c0 + c1
    n |= (1 << p)
    n &= ~((1 << p) - 1)
    n |= (1 << (c1 - 1)) - 1

    return n


if __name__ == "__main__":
    n = 5  # binary: 101
    result = next_higher_with_same_ones(n)
    print("Expected:", 6)  # binary: 110
    print("Output:", result)
