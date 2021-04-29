#!/bin/python3

import os


def counting_valleys(steps, path):
    """ Returns the number of valleys traversed by a hiker
        A valley starts when the hiker steps down to sea
        level and end when he steps up to sea level """

    valleys = 0
    altitude = 0

    for step in path:
        if step == 'U':         # Step up, altitude goes up
            altitude += 1
            if altitude == 0:   # If sea level is reached from a step up
                valleys += 1    # the hiker must have gone through a valley

        else:                   # Step down, altitude goes down
            altitude -= 1

    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_steps = int(input().strip())
    up_down_path = input()              # Each step is either 'U' up, or 'D' down

    result = counting_valleys(num_steps, up_down_path)

    fptr.write(str(result) + '\n')
    fptr.close()
