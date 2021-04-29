from functools import cmp_to_key


class Player:
    def __init__(self, name, score):    # Initialise name and score
        self.name = name
        self.score = score

    def __repr__(self):
        for a in range(len(data)):
            data[a] = name, score   # Display a person as (name, score)
            data[b] = data[a + 1]   # Display a second person in the same way

    def comparator(a, b):
        """ Returns the keys for the comparator """

        if a.score < b.score:
            return 1
        elif a.score == b.score and a.name > b.name:
            return 0
        else:
            return -1


if __name__ == '__main__':
    n = int(input())
    data = []

    for _ in range(n):
        name, score = input().split()
        score = int(score)

        player = Player(name, score)
        data.append(player)

    data = sorted(data, key=cmp_to_key(Player.comparator))

    for person in data:
        print(person.name, person.score)
