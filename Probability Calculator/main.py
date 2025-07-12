import copy
import random

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for key,value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self,number_to_draw):
        new_list=[]

        if number_to_draw > len(self.contents):
            new_list = copy.deepcopy(self.contents)
            self.contents.clear()
            return new_list
        else:
            for _ in range (number_to_draw):
                new_list.append(self.contents.pop(random.randint(0,len(self.contents)-1)))
        return new_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    N = 0
    for _ in range(num_experiments):
        i = 0
        experiment_hat = copy.deepcopy(hat) 
        experiment_draw = experiment_hat.draw(num_balls_drawn)
        for color,amount in expected_balls.items():
            if color in experiment_draw:
                number = experiment_draw.count(color)
                if number >= amount:
                    i += 1
        if i == len(expected_balls):
            N += 1
    return N/ num_experiments


hat = Hat(black=6, red=4, green=3)
print(experiment(hat = hat,expected_balls={'red':2,'green':1},num_balls_drawn=5,num_experiments=2000))