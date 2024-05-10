from learntools.core import binder
binder.bind(globals())
from learntools.game_ai.ex3 import *
import inspect
import os

num_leaves = 7*7*7
selected_move = 3


def my_agent(obs, config):
    # Your code here: Amend the agent!
    import random
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    return random.choice(valid_moves)


def write_agent_to_file(function, file):
    with open(file, "a" if os.path.exists(file) else "w") as f:
        f.write(inspect.getsource(function))
        print(function, "written to", file)

write_agent_to_file(my_agent, "submission.py")

