def info_print():
    print("请选择功能")
    print("1.添加学员")
    print("2.删除学员")
    print("3.修改学员")
    print("4.查询学员")
    print("5.显示所有学员")
    print("6.推出系统学员")
    print('-'*20)

info_print()

while(True):

    user_num= int(input('请输入功能序号:'))

    if user_num==1:
        print("添加")
    elif user_num==2:
        print("删除")
    elif user_num==3:
        print("修改")
    elif user_num==4:
        print("查询")
    elif user_num==5:
        print("显示所有")
    elif user_num==6:
        break