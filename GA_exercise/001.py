import matplotlib.pyplot as plt
import numpy as np
#这个变量代表的是感染率，感染人数/总人数
infection_rate = 0

#社会上依然存在着的感染人数
infection_pop_arr_society = []
#隔离且感染着的人数
isolation_pop_arr = []
#隔离+社会全部的感染人数
infection_pop_arr = []


#建立一个数组用来存放政策，也就是政策的list，目前仅仅存在动态清零和躺平两种
policies=["dynamicZero","herdImmunity"]

#GA的步骤
#首先是种群初始化，但是目前只有两种，就生成两个种群，10和01，这里是二择其一的，不能有11存在，但是00可以存在，就是完全不管，任由变异
#所以可以简化为选择唯一的1所在的坐标。

#然后就是适应度函数——采取了任何的策略一定会对于传染率有着影响，以及传染人群，当然假设目前病毒不会产生任何变异的情况
#具体的影响？
#首先第一天，病毒出现，然后感染百分比增高，假设病毒每一次周期固定感染2%，那么如果是动态清零的政策，则
#
population = 100000

infection_popu = 1
isolation_pop = 0

infection_rate_arr = []
time=[]
date = 30
def fitness(infection_rate_prev,infection_rate_cur):
    if(infection_rate_prev-infection_rate_cur>0.003 or infection_rate_cur>=0.003):
        return 0
    else:
        return 1


def initTime(time,date):
    ans = time+[0]*(date-len(time))
    return ans

def initInfectionRate(infection_rate_arr,date):
    ans = infection_rate_arr+[0]*(date-len(infection_rate_arr))
    return  ans

def initInfectionSocietyPopArr(infection_pop_arr_society, date):
    ans = infection_pop_arr_society + [0] * (date - len(infection_pop_arr_society))
    return ans


def initInfectionPopArr(infection_pop_arr, date):
    ans = infection_pop_arr + [0] * (date - len(infection_pop_arr))
    return ans

def initIsolationPopArr(isolation_pop_arr,date):
    ans = isolation_pop_arr+[[0]*3]*(date-len(isolation_pop_arr))
    return ans


def updateIsolationPopArr(isolation_pop_arr):
    for i in range(len(isolation_pop_arr)):
        if(isolation_pop_arr[i][2]!=0):
            isolation_pop_arr[i]= list(isolation_pop_arr[i])
            isolation_pop_arr[i][2] = isolation_pop_arr[i][2]-1

def getInfectionPopToday(isolation_pop_arr,infection_popu):
    isolation_pop = 0;
    for isolation in isolation_pop_arr:
        if(isolation[2]!=0):
            isolation_pop = isolation_pop+isolation[1]
    return isolation_pop+infection_popu

def simulate(infection_rate, policies, population, infection_popu, date, infection_rate_arr, time, infection_pop_arr_society, isolation_pop_arr, isolation_pop,infection_pop_arr):
    time= []
    time = initTime(time,date)
    infection_rate_arr = []
    infection_rate_arr = initInfectionRate(infection_rate_arr,date)
    infection_pop_arr_society = []
    infection_pop_arr_society = initInfectionSocietyPopArr(infection_pop_arr_society, date)
    isolation_pop_arr = [[0,0,0]]
    isolation_pop_arr = initIsolationPopArr(isolation_pop_arr,date)
    infection_pop_arr = []
    infection_pop_arr = initInfectionPopArr(infection_pop_arr,date)

    policy = ""
    for i in range(0, date):
        time[i] = i
        infection_rate_prev = infection_rate
        infection_popu = infection_popu * 2
        infection_rate_cur = infection_popu / population
        infection_rate_arr[i] = infection_rate_cur
        infection_pop_arr_society[i] = infection_popu
        updateIsolationPopArr(isolation_pop_arr)
        if(policy=="dynamicZero"):
            policy = "dynamicZero"
            isolation_pop = infection_popu * 0.7
            infection_popu = infection_popu * 0.3
            isolation_pop_arr[i] = (i,isolation_pop,14)


        else:
            policy = policies[fitness(infection_rate_prev, infection_rate_cur)]

        infection_cur_day_all = getInfectionPopToday(isolation_pop_arr,infection_popu)

        infection_pop_arr[i] = infection_cur_day_all




    # 然后制图，横坐标是时间，纵坐标是传染率
    plt.figure()
    plt.plot(time, infection_pop_arr)
    # plt.yticks(np.arange(0.1,0.2,0.05))
    plt.show()

def main():
    simulate(infection_rate, policies, population, infection_popu, date, infection_rate_arr, time, infection_pop_arr_society, isolation_pop_arr, isolation_pop,infection_pop_arr)

if __name__ == '__main__':
    main()



