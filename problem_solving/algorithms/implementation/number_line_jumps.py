#!/bin/python3

import os


def kangaroo(pos_1, vel_1, pos_2, vel_2):
    """ Given the initial positions and velocities of two
        kangaroos determine whether or not they can be at
        the same location at the same time """

    for i in range(1, 10000):
        pos_1 = pos_1 + vel_1
        pos_2 = pos_2 + vel_2

        if pos_1 == pos_2:  # If yes, no need to continue
            return 'YES'

    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pos_and_vel = input().split()

    position_1 = int(pos_and_vel[0])
    velocity_1 = int(pos_and_vel[1])

    position_2 = int(pos_and_vel[2])
    velocity_2 = int(pos_and_vel[3])

    result = kangaroo(position_1, velocity_1, position_2, velocity_2)

    fptr.write(result + '\n')
    fptr.close()
