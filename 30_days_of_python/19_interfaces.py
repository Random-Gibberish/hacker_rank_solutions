class AdvancedArithmetic(object):
    def divisor_sum(self, num):         # Default function
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisor_sum(self, num):         # Override default function
        """ Returns the sum of a numbers divisors """

        div_sum = 0

        for i in range(1, num + 1):
            try:
                if num % i == 0:        # If i is a divisor of num
                    div_sum += i        # add it to the current sum of num's divisors
            except div_sum == 0:        # Otherwise implement the default function
                div_sum = AdvancedArithmetic()

        return div_sum


if __name__ == '__main__':
    number = int(input())

    my_calculator = Calculator()
    sum_div = my_calculator.divisor_sum(number)

    print("I implemented: " + type(my_calculator).__bases__[0].__name__)
    print(sum_div)
