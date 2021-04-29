
def minimum_index(seq):
    """ Returns the minimum index of an array """

    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")

    min_idx = 0

    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i

    return min_idx


# Classes to be tested. Return arrays of varying lengths
class TestDataEmptyArray(object):
    @staticmethod
    def get_array():
        return []


class TestDataUniqueValues(object):
    @staticmethod
    def get_array():
        return [3, 1, 2]

    @staticmethod
    def get_expected_result():
        return 1


class TestDataExactlyTwoDifferentMinimums(object):
    @staticmethod
    def get_array():
        return [5, 7, 2, 8, 2]

    @staticmethod
    def get_expected_result():
        return 2


# Testing functions, one for each class
def test_with_empty_array():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def test_with_unique_values():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def test_with_exactly_two_different_minima():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


if __name__ == '__main__':
    test_with_empty_array()
    test_with_unique_values()
    test_with_exactly_two_different_minima()
    print("OK")
