
import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.ball_dict = kwargs.copy()                  # add the dictionary to a... new dictionary
        self.contents = []                              # ready a list
        for key, value in self.ball_dict.items():       # get keys and values of dict
            for ball_indv_str in range(0, value):
                self.contents.append(key)               # add string of key to list
        self.full_contents = self.contents.copy()       # keep a full list so you can refresh (copy so chnage of one does not affect the other
    def draw(self, N_balls):
        drawn_balls = []
        for i_draw in range (0, N_balls):               # how many of those sweet balls you need?
            if self.contents == []:                     # do the contents need refreshing?
                self.contents = self.full_contents.copy()
            ball_chosen = random.choice(self.contents)  # pick a random ball
            self.contents.remove(ball_chosen)           # then remove the first instance
            drawn_balls.append(ball_chosen)             # append it to the new ball list
        return drawn_balls

# hat.balls.values()
# hat.balls['red']/sum(hat.balls.values())
#



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    Success_count = 0
    for i_exp in range(0, num_experiments):
        hat.contents = hat.full_contents.copy()
        check_bool = []
        Ball_list = hat.draw(num_balls_drawn)
        for key, value in expected_balls.items(): #list of ball pattern needing to be drawn
            count = 0
            for ele in Ball_list:
                if (ele == key):
                    count += 1
            if count >= value:
                check_bool.append(True)
            else:
                check_bool.append(False)
        if all(check_bool):
            Success_count += 1
    probability = Success_count / num_experiments
    return probability



    # for i_N_ball in range(0, num_balls_drawn):


class Juliee:
    def __init__(self):
        Dating_Juliee = True

Eric = 0
in_Love_With_Juliee = 0

while Eric is in_Love_With_Juliee:
    Notes = Notes +1
    if Juliee == Munching_On_Fingers
        Eric_Laugh = True
    in_Love_With_Juliee = days_left - 1
