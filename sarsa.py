from game import game
from view import view
import random

def q_max(q, state):
    '''
    q_max : Q値の最大値をとるタイプ（index）を返す．
            ε-greedyで使用
    '''
    maximum = [i for i, x in enumerate(q[state]) if x == max(q[state])]
    return maximum[random.randint(0, len(maximum) - 1)]

def epsilon_greedy(state):
    '''
    ε-greedy
    '''
    epsilon = 0.3
    greedy = random.random()
    a = 0
    if(epsilon > greedy):
        a = q_max(Q, state)
    else:
        a = random.randint(0, 14)
    return a

GAMMA = 0.9
ALPHA = 0.1

if __name__ == "__main__":
    
    gamesystem = game()
    Q = [[0 for i in range(15)]for j in range(15)]
    
    for i in range(100):    
        gamesystem.Initialize()
        state = gamesystem.GetState()
        action = epsilon_greedy(state)
        while not(gamesystem.IsEnd()):
            reward = gamesystem.Act(action)
            next_state = gamesystem.GetState()
            next_action = epsilon_greedy(next_state)
            Q[state][action] += ALPHA * (reward + GAMMA * Q[next_state][next_action] - Q[state][action])
            state = next_state
            action = next_action
    
    for raw in Q:
        print(raw)
    view(Q)