from game import game
import random

gamesystem = game()
Q = [[0 for i in range(15)]for j in range(15)]


def q_max()
    '''
    q_max
    '''
    

def epsilon_greedy():
    '''
    ε-greedy
    '''
    epislon = 0.3
    greedy = random.random()
    if(epsilon > greedy):
        a = q_max(gamesystem.compatibilities[][])
    else:
        a = random.randint(0, 14)
    return a

'''
sarsa
'''
for i in range(10):
    gamesystem.Initialize()
    state = gamesystem.GetState()
    next_state = 
    reward = gamesystem.Act(next_state)
    Q[state][next_state] += alpha * (reward + ganma * Q[next_state][next_action] - Q[state][next_state]
