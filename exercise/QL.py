
GAMMA = 0.8
R = [
    [-1, -1, -1, -1, 0, -1],
    [-1, -1, -1, 0, -1, 100],
    [-1, -1, -1, 0, -1, -1],
    [-1, 0, 0, -1, 0, -1],
    [0, -1, -1, 0, -1, 100],
    [-1, 0, -1, -1, 0, 100]
]

Q = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]


def getMaxQ(state):
    return max(Q[state])


def QLearning(state):
    curAction = None

    for action in range(6):
        if(R[state][action] == -1):
            Q[state][action] = 0
        else:
            curAction = action
            Q[state][action] = R[state][action]+GAMMA * getMaxQ(curAction)



def main():
    count = 0
    while count < 200:
        for i in range(6):
            QLearning(i)
        count=count+1

    print(Q)

if __name__ == '__main__':
    main()




