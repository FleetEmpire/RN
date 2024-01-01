import random


class RandomNumberCore:
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop
        self.ranges = list(range(start, stop + 1))

    def random_number_list_choice(self):
        return random.choice(self.ranges)

    def random_number_fast(self):
        return random.randrange(self.start, self.stop + 1)


class RandomNumber_except(RandomNumberCore):
    def __init__(self, start, stop):
        super().__init__(start=start, stop=stop)

    def random_number_except(self, *except_numbers):
        for n in except_numbers:
            self.ranges.remove(n)
        return self.random_number_list_choice()


if __name__ == '__main__':
    for i in range(1, 52):
        N = RandomNumber_except(1, 51)
        print(N.random_number_except(15, 16, 41))
