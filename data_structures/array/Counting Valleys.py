import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    vally_count = 0
    level = 0
    for i in range(steps):
        prev_level = level
        if path[i] == 'U':
            level += 1

        if path[i] == 'D':
            level -= 1
        if prev_level == 0 and level == -1:
            vally_count += 1
    return vally_count

if __name__ == '__main__':
    steps=8
    path='UDDDUDUU'
    result = countingValleys(steps, path)
    print(result)