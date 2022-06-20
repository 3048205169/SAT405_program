import random

import numpy as np

data = [(1, 2, 4), (1, 3, 10), (1, 4, 2), (2, 3, 3), (2, 4, 9), (3, 4, 5)]


def initPopulation():
    result = []

    for i in range(0,800):
        tmp = [1, 2, 3, 4]
        np.random.shuffle(tmp)
        result.append(tmp)
    return result

def roulette(relatedFit,population,population_new):
    for i in range(0,len(relatedFit)):
        prop = random.random()
        if (relatedFit[i]>=prop):
            population_new.append(population[i])


def searchDist(first,second):
    for item in data:
        if (item[0]==first and item[1]==second):
            return item[2]

    pass
def dist(item):
    #todo
    distSum = 0
    for i in range(0,4):
        if(i<=2):
            first = i
            second = i+1
            if (item[first]<=item[second]):
                distSum = distSum + searchDist(item[first], item[second])
            else:
                distSum = distSum + searchDist(item[second],item[first])


        else:
            first = i
            second = 0
            if (item[first] <= item[second]):
                distSum = distSum + searchDist(item[first], item[second])
            else:
                distSum = distSum + searchDist(item[second], item[first])

    return distSum


def select(population,population_new):
    distanceArr = []
    for item in population:
        distance = dist(item)
        distanceArr.append(distance)


    distanceMax = max(distanceArr);

    fitnessArr = []

    for i in distanceArr:
        fitnessArr.append(distanceMax-i)

    sumFit = sum(fitnessArr)
    avgFit = sumFit/len(fitnessArr)

    for i in range(0,len(population)):
        if(fitnessArr[i]>=avgFit):
            population_new.append(population[i])


    print("max fit= ",max(fitnessArr))

    return fitnessArr
    # roulette(relatedFit,population,population_new)#轮盘赌





def mutate(population,population_ne):
    pass




def main():
    print("GA computing TSP")
    population = initPopulation()

    population_new = []



    while(len(population)>=3):
        fitnessArr = select(population,population_new)
        population = population_new
        population_new = []
        if (max(fitnessArr)==min(fitnessArr)):
            break
        mutate(population,population_new)

    print(population)






if __name__ == '__main__':
    main()