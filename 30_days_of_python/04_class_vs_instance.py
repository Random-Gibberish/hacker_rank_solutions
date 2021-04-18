
class Person:
    def __init__(self, initial_age):
        """ Initiates initial_age and deals with invalid input """

        self.initial_age = initial_age

        if self.initial_age < 0:
            self.initial_age = 0
            print('Age is not valid, setting age to 0.')

    def am_i_old(self):
        """ Determines whether a person is young,
            a teenager or old """

        if self.initial_age < 13:
            print('You are young.')
        elif self.initial_age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')

    def year_passes(self):
        """ Increments age as a year pass """

        self.initial_age += 1
