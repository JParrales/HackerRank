#!/bin/python3

if __name__ == '__main__':
    n = int(input())
    out = []
    out = [x for x in range(1, n+1)]

    print (*out, sep = '')