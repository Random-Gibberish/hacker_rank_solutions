class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximum_difference = None

    def compute_difference(self):
        """ Returns the maximum difference
            between elements in the array """

        self.maximum_difference = abs(max(array) - min(array))


if __name__ == '__main__':
    _ = input()
    array = [int(e) for e in input().split(' ')]

    d = Difference(array)
    d.compute_difference()

    print(d.maximum_difference)
