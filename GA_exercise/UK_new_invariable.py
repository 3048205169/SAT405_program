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

policy = ("herdImmunity",herdImmunity)
infection_popu_society = 1
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
date = 50

infection_new_limit = 10000
#相比于中国需要增加经济因素