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
#数组存储每日经济代价
econ_cost_per = []
#数组存储截止到当日总代价
econ_cost_per_sum = []
#这边每人的经济代价实际上可以是4379¥这种数字，但是，这里可以是一种比例，通过这个比例来计算，然后调整参数从而确定政府的fitness函数的阈值
per_cost = 1

#群体免疫政策持续时间
herdImmunity = 3
#动态清零政策持续时间
dynamicZero = 3

initPolicy = ("herdImmunity",herdImmunity)
R0=3

#存储每日的新增感染人数
infection_pop_new = []

#建立一个数组用来存放政策，也就是政策的list，目前仅仅存在动态清零和躺平两种
policies = ["dynamicZero", "herdImmunity"]

#GA的步骤
#首先是种群初始化，但是目前只有两种，就生成两个种群，10和01，这里是二择其一的，不能有11存在，但是00可以存在，就是完全不管，任由变异
#所以可以简化为选择唯一的1所在的坐标。

#然后就是适应度函数——采取了任何的策略一定会对于传染率有着影响，以及传染人群，当然假设目前病毒不会产生任何变异的情况
#具体的影响？
#首先第一天，病毒出现，然后感染百分比增高，假设病毒每一次周期固定感染2%，那么如果是动态清零的政策，则
#
population = 1000000

init_infection_popu = 1
isolation_pop = 0

infection_rate_arr = []
time=[]
date = 30

#相比于中国需要增加经济因素

def fitness(infection_popu_society,policy,econ_cost):
    #放任自流
    if policy[0] == "herdImmunity":
        if (infection_popu_society>= 750):
            return (policies[0],dynamicZero)
        else:
            return (policies[1],herdImmunity)
        #如果是动态清零

    # 如果经济代价超过阈值，则实现开放经济也就是herdImmunity
    if econ_cost > 4000:
        return (policies[1],herdImmunity)
    if(policies[0]==policy[0]):
        return (policies[0],dynamicZero)
    else:
        return (policies[1],herdImmunity)




def setTime(date):
    ans = []
    for i in range(0,date):
        ans = ans + [i]
    return ans

def setZeroArr(date):
    ans = [0]*date
    return ans

def setIsolationPopArr(isolation_pop_arr, date):
    #生成全0数组
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

def setInfectionPopNewArr():
    ans = infection_rate_arr + [0] * (date - len(infection_rate_arr))
    return ans





def simulate(infection_rate, policies, population, init_infection_popu, date, infection_rate_arr, time, infection_pop_arr_society, isolation_pop_arr, isolation_pop,infection_pop_arr,initPolicy,R0,econ_cost_per,econ_cost_per_sum):
    #初始化数据，以下数据结构是为了方便plot制图，记录数据
    #将infection_pop_new变为全部为0的数组
    infection_pop_new = setZeroArr(date)
    #将infection_rate_arr构造为全部为0的数组
    infection_rate_arr = setZeroArr(date)
    #将infection_pop_arr_society构造为全部为0的数组
    infection_pop_arr_society = setZeroArr(date);
    #将isolation_pop_arr构造为全部为[0,0,0]的数组
    isolation_pop_arr = [[0,0,0]]
    isolation_pop_arr = setIsolationPopArr(isolation_pop_arr, date)
    #将infection_pop_arr构造为全部为0的数组
    infection_pop_arr = setZeroArr(date)
    #将econ_cost_per构造为全为0的数组
    econ_cost_per = setZeroArr(date)
    #econ_cost_per_sum构造为全为0的数组
    econ_cost_per_sum = setZeroArr(date)


    #将policy初始化为initPolicy也就是传入的policy
    policy = initPolicy
    infection_popu = init_infection_popu#当天总传染人数
    infection_popu_society = infection_popu#当天社会传染人数
    isolation_pop = infection_popu-infection_popu_society#当天隔离人数
    infection_rate_cur = init_infection_popu / population#目前感染率的初始化：初始化感染人数/总人数




    for i in range(0, date):
        infection_rate_prev = infection_rate

        infection_popu_new = infection_popu_society*R0

        # if(infection_popu_new >= 20000):
        #     infection_popu_new = 20000

        infection_pop_new[i] = infection_popu_new

        infection_popu_society = infection_popu_society*(1+R0);#当天社会感染人数根据R0值翻倍


        econ_cost = 0

        if(policy[0] == "dynamicZero"):
            #严格的动态清零政策
            isolation_pop = infection_popu_society * 0.7#当天隔离人数=当天社会感染人数*0.7
            econ_cost = per_cost * isolation_pop
            econ_cost_per[i] = econ_cost
            econ_cost_per_sum[i] = sum(econ_cost_per)
            infection_popu_society = infection_popu_society * 0.1#没有被抓去隔离的当天社会感染者依然在传播病毒
            isolation_pop_arr[i] = (i,isolation_pop,14)#此处存疑，目的是做一下记录


        econ_cost_sum = econ_cost_per_sum[i]


        infection_popu = infection_popu_society + isolation_pop    # 当天感染总人数=当天社会感染人数 + 隔离者人数

        infection_pop_arr[i] = infection_popu#记录当天感染总人数

        infection_rate_cur = infection_popu / population#当天感染率=当天感染总人数/人口

        infection_rate_arr[i] = infection_rate_cur  #记录当天感染率

        infection_pop_arr_society[i] = infection_popu_society  #记录当天社会感染总人数

        updateIsolationPopArr(isolation_pop_arr)  # 特殊的数据结构


        if(policy[1]==0):
            policy = fitness(infection_popu_society,policy,econ_cost_sum)
            # policy = policies[fitness(infection_popu_society,policy,econ_cost_sum)]
        else:
            policy = (policy[0],policy[1]-1)




    # 然后制图，横坐标是时间，纵坐标是传染率
    time = setTime(date)#todo此处要重写setTime，将time变成[1,2,3,4,5,6,7,.....]
    plt.figure()
    plt.plot(time,infection_pop_new)
    # plt.grid(True,linestyle="--",alpha=0.5)
    plt.xlabel("period")
    plt.ylabel("newly infected population")
    title = "UK COVID-19 epidemic prevention and control with economic"
    plt.title(title)
    # plt.plot(time, infection_pop_arr)
    # plt.plot(time,isolation_pop_arr)
    plt.yticks(np.arange(0.0,10000,1))
    plt.savefig(title+".jpg")
    plt.show()

def main():
    simulate(infection_rate, policies, population, init_infection_popu, date, infection_rate_arr, time, infection_pop_arr_society, isolation_pop_arr, isolation_pop, infection_pop_arr,initPolicy,R0,econ_cost_per,econ_cost_per_sum)

if __name__ == '__main__':
    main()



