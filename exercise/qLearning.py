import random

import numpy.random



def main():
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

    target = 5

    count = 0
    gama = 0.8

    while count<=1000:
        s = numpy.random.randint(0,6)
        a = getA(s,R)
        print("start=======================")
        while(a!=target):
            s_new = a

            a_new = getMax(Q,R,a)

            Q[s][a] = R[s][a] + gama * Q[s_new][a_new]
            s = s_new
            a = a_new
            print(Q)
            print(s_new,a_new)

        count = count+1



def getMax(Q,R,a):
    candidate = []
    for item in range(0,len(R[a])):
        if (R[a][item]!=-1):
            candidate.append(item)
    a_new = candidate[0]
    maxValue = Q[a][candidate[0]]
    maxValueArr = []
    for i in candidate:
        if (Q[a][i]>=maxValue):
            maxValue = Q[a][i]

    for i in range(0,len(candidate)):
        if (Q[a][candidate[i]]==maxValue):
            maxValueArr.append(candidate[i])


    a_new = maxValueArr[numpy.random.randint(0,len(maxValueArr))]
    return a_new









def getA(s,R):
    candidate = []
    for item in range(0,len(R[s])):
        if (R[s][item]!=-1):
            candidate.append(item)

    a = candidate[random.randint(0,len(candidate)-1)]
    return a

if __name__ == '__main__':
    main()