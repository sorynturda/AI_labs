import random


class SearchProblem:
    def __init__(self, n, x0, y0, x_goal, y_goal):
        self.n = n
        self.x0 = x0
        self.y0 = y0
        self.x_goal = x_goal
        self.y_goal = y_goal

    def get_initial_state(self):
        return self.x0, self.y0

    def is_goal(self, state):
        return self.x_goal == state[0] and self.y_goal == state[1]

    def get_successors(self, state):
        """ Only the legal actions from the given state . It
            returns a list of pairs ( action , state ) , where a state
            is (x , y ) , and action is one of up , down , left , right .
        """

        d = {'UP': ((state[0] - 1, state[1]), 'up'),
             'DOWN': ((state[0] + 1, state[1]), 'down'),
             'LEFT': ((state[0], state[1] - 1), 'left'),
             'RIGHT': ((state[0], state[1] + 1), 'right')}

        if state[0] == 0 and state[1] == 0:
            return [d['DOWN'], d['RIGHT']]
        if state[0] == self.n - 1 and state[1] == 0:
            return [d['UP'], d['RIGHT']]
        if state[0] == 0 and state[1] == self.n - 1:
            return [d['LEFT'], d['DOWN']]
        if state[0] == self.n - 1 and state[1] == self.n - 1:
            return [d['LEFT'], d['UP']]
        if state[0] == 0:
            return [d['RIGHT'], d['DOWN'],d['LEFT']]
        if state[0] == self.n - 1:
            return [d['UP'], d['LEFT'], d['RIGHT']]
        if state[1] == 0:
            return [d['UP'], d['DOWN'], d['RIGHT']]
        if state[0] == self.n - 1:
            return [d['UP'], d['DOWN'], d['LEFT']]
        return [d['UP'], d['DOWN'], d['LEFT'], d['RIGHT']]



    def do_path(self, path, state):
        """ starting from the given state , execute the path of
        actions and print the final state . the path is a list
        of actions """
        path.append(state)
        path.append(random.choice(self.get_successors(state)))
        while True:
            if self.is_goal(path[-1][0]):
                break
            path.append(random.choice(self.get_successors(path[-1][0])))

        return path



n = 10
sp = SearchProblem(n, 0, 0, 5, 5)

res = sp.do_path([], sp.get_initial_state())
print(res)
print(len(res))
