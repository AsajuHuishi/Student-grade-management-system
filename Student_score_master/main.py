# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import utils
import random
# 不提示警告
pd.set_option('mode.chained_assignment', None)
seed = 99
np.random.seed(seed)  # Numpy module.
random.seed(seed)  # Python rando7m module.
##给每个人添加随机成绩（80-100）：
def get_data():
    content = pd.read_excel('shizuo.xlsx')
    num = content.shape[0]
    score = np.random.randint(80,101,(num,1))
    content['成绩'] = score
    return content

###
def console(obj):
    print('Student grade management system'.center(35,'-'))
    print('|1.increase student records'.ljust(35,'-')+'|')
    print('|2.modify student records'.ljust(35,'-')+'|')
    print('|3.delete student records'.ljust(35,'-')+'|')
    print('|4.inquire by name or id'.ljust(35,'-')+'|')
    print('|5.sort by C Language scores'.ljust(35,'-')+'|')
    print('|6.statistic'.ljust(35,'-')+'|')
    print('|7.exit'.ljust(35,'-')+'|')
    while(1):
        message = int(input('please select(1-7):'))
        if message>7 or message<1:
            print('Wrong input!')
        elif message==1:
            stu_id = input('学生学号:')
            stu_name = input('学生姓名:')
            stu_score = input('学生成绩:')
            obj.add_new_info(stu_id,stu_name,stu_score)
        elif message==2:
            m = input('modify what:(1:student id 2:student score)')
            if m == '1':
                stu_name = input('学生姓名:')
                stu_id = input('要更改的学生学号:')
                obj.mod_id_by_name(stu_name,stu_id)
            elif m == '2':
                stu_name = input('学生姓名:')
                stu_score = input('要更改的学生成绩:')
                obj.mod_score_by_name(stu_name,stu_score)
            else:
                print('Wrong input!')
        elif message==3:
            mn = input('要删除的学生姓名:')
            obj.del_info_by_name(mn)
        elif message==4:
            m = input('inquire by:(1:student id 2:student name)')
            if m == '1':
                stu_id = input('要查询的学生学号:')
                obj.find_score_by_id(stu_id)
            if m == '2':
                stu_name = input('要查询的学生姓名:')
                obj.find_score_by_name(stu_name)   
            else:
                print('Wrong input!')
        elif message==5:
            obj.sort_by_score()
        elif message==6:
            obj.statistic()
        else:
            content = obj.ret()
            break
    return content
#obj1.add_new_info('B195A6019', '刘明熙', 88)
#obj1.mod_id_by_name('冯雪晴', 'B195A6052')     
#obj1.mod_score_by_name('张子蕙', 99)
#obj1.del_info_by_name("姚柏文")
    
def main():
    content = get_data()
    ####创建对象
    obj1 = utils.Manage(content)
    content = console(obj1)
    ###保存表格
    content.to_excel('完整表.xlsx', index=False)

if __name__ == '__main__':
    main()