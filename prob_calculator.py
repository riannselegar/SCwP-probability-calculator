import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = sum([[k]*v for k, v in kwargs.items()], [])
        self.originalContent = copy.copy(self.contents)

    def draw(self, num):
        if num > len(self.contents):
            num = len(self.contents)

        if len(self.contents) == 0:
            return "Nenhuma bola a remover"

        removed = random.sample(self.contents, num)
        returnString = copy.copy(removed)

        self.contents = [i for i in self.contents if not i in removed or removed.remove(i)]

        return returnString


def compareDicts(expected, given):
    for key, value in expected.items():
        if key in given:
            if value > given[key]:
                return False
        else:
            return False

    return True

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    getExpectedBalls = 0

    for i in range(num_experiments):
        temporaryHat = copy.copy(hat)
        removedBalls = temporaryHat.draw(num_balls_drawn)
        counter = {}
        for ball in removedBalls:
            counter[ball] = counter.get(ball, 0) + 1

        if compareDicts(expected_balls, counter):
            getExpectedBalls += 1

    return getExpectedBalls/num_experiments