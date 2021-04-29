import math as ma


def angle_theta(ab, bc):
    """ Returns the angle MBC of a triangle ABC given:
         . the lengths AB and BC
         . M is the midpoint of the hypotenuse AC """

    theta = round(ma.degrees(ma.atan2(ab, bc)))

    # chr(176) = 'º' the degree symbol
    return str(theta) + chr(176)


if __name__ == '__main__':
    len_ab = int(input())
    len_bc = int(input())

    result = angle_theta(len_ab, len_bc)
    print(result)
