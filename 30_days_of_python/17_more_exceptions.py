class Calculator:
    @staticmethod
    def power(number, power):
        """ Returns a number to a given power of both are
            greater than zero. Raises an exception otherwise """

        if number < 0 or power < 0:
            raise Exception('n and p should be non-negative')
        else:
            return pow(number, power)


if __name__ == '__main__':
    my_calculator = Calculator()
    T = int(input())

    for i in range(T):
        n, p = map(int, input().split())

        try:
            ans = my_calculator.power(n, p)
            print(ans)

        except Exception as e:
            print(e)
