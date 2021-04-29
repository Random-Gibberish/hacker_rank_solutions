import cmath as cm

if __name__ == '__main__':
    n = complex(input())    # Complex number in the form z = x + iy

    # Polar coordinates of n
    print(abs(n))           # Absolut distance from origin
    print(cm.phase(n))      # Counter-clockwise angle in radians

