#!/usr/bin/python3
import sys

ans = 0
n = len(sys.argv)

for i in range(1, n):
    ans = ans + int(sys.argv[i])
print('{:d}'.format(ans))
