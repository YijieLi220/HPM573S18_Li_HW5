import figure as cls
import random

class Game:
    def __init__(self, id):
            self.id = id

    def simulation(self):
        x = -250
        i = 0
        j = 0
        step = ["H", "T", "H", "T", "H", "T", "H", "T", "H", "T", "H", "T", "H", "T", "H", "T", "H", "T", "H",
                    "T"]  # Create a list.
        for j in range(0, len(step)):
            step[j] = random.choice(["H", "T"])  # P(H)=0.5, P(T)=0.5
            j = j + 1
        for i in range(0, 18):
            if step[i] == 'T' and step[i + 1] == 'T' and step[i + 2] == 'H':
                x += 100
                i = i + 3
            else:
                x += 0
                i = i + 1
        return x

class Cohort:
    def __init__(self, id, pop_size):

        self.step = []
        self.total_score = []
        n = 1
        while n <= pop_size:
            gameunit = Game(id * pop_size + n)
            self.step.append(gameunit)
            n += 1

    def simulatecohort(self):
        for game in self.step:
            value = game.simulation()
            self.total_score.append(value)

    def get_expected_score(self):
        return sum(self.total_score) / len(self.total_score)

test = Cohort(2, 1000)
test.simulatecohort()
print("The expected score is", test.get_expected_score())
result = test.total_score
maxscore=max(result)
minscore=min(result)
cls.graph_histogram(
    observations=result,
    title='Histogram',
    x_label='Values',
    y_label='Counts',
    legend='Number of flips')

count=0
for i in range(0,len(result)):
    if result[i]<0:
        count+=1
    else:
        count+=0
probability=count/float(1000)
print('The probability of losing money is',probability)
