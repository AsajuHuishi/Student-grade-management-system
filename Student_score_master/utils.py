import pandas as pd
import numpy as np
##1.增加学生记录
class Manage():
    def __init__(self,content):
        self.content = content
          
    def ret(self):
        return self.content
    
    def add_new_info(self, student_id1, name1, score1):
    #student_id1 = 'B195A6019'
    #name1 = '刘明熙'
    #score1 = 88
        list1 = np.array([student_id1, name1, score1]).reshape((1,3))
        new1 = pd.DataFrame(list1, columns = self.content.columns)
        #此时list1都是字符串，88应该转换为整型
        new1['成绩'] = pd.to_numeric(new1['成绩'])
        #合并
        self.content = pd.concat((self.content,new1))
        #每修改一次，重建索引
        self.content = self.content.reset_index(drop=True)
    
    ##2.修改学生记录
    #修改冯雪晴的学号
    def mod_id_by_name(self, name, new_id):
        namelist = self.content['姓名'].tolist()
        if name in namelist:
            find = self.content[self.content['姓名']==name].index.tolist()
            for i in find:#万一有重名的
                self.content['学号'][i] = new_id
            self.content = self.content.reset_index(drop=True)
        else:
            print("No such name.")    
       
    
    #修改某个人的成绩
    def mod_score_by_name(self, name, new_score):
        namelist = self.content['姓名'].tolist()
        if name in namelist:
            find = self.content[self.content['姓名']==name].index.tolist()
            for i in find:
                self.content['成绩'][i] = new_score
            self.content = self.content.reset_index(drop=True)
        else:
            print("No such name.")    

        
    ##3.删除某个人例如姚柏文的记录
    def del_info_by_name(self, name):
        namelist = self.content['姓名'].tolist()
        if name in namelist:
            find = self.content[self.content['姓名']==name].index.tolist()
            #drop0行1列
            for i in find:
                self.content = self.content.drop(i)
            self.content = self.content.reset_index(drop=True)
        else:
            print("No such name.")    

    #按姓名查询成绩
    def find_score_by_name(self,name):
        namelist = self.content['姓名'].tolist()
        if name in namelist:
            find = self.content[self.content['姓名']==name].index.tolist()
            print("姓名:%s 学号:%s 成绩:%d"%(name,self.content['学号'][find[0]],self.content['成绩'][find[0]]))
        else:
            print("No such name.")
    
    #按学号查询成绩
    def find_score_by_id(self,idd):
        idlist = self.content['学号'].tolist()
        if idd in idlist:
            find = self.content[self.content['学号']==idd].index.tolist()
            print("姓名:%s 学号:%s 成绩:%d"%(self.content['姓名'][find[0]],idd,self.content['成绩'][find[0]]))
        else:
            print("No such id.")        
    #find_score_by_name()
    #find_score_by_id()
    
    ##按成绩排序,从大到小排序
    def sort_by_score(self):
        self.content = self.content.sort_values('成绩',ascending=False)
        self.content = self.content.reset_index(drop=True)
    
    ##统计成绩最大最小值，平均值，中位数，众数
    def statistic(self):
        #先降序排列
        temp = self.content.sort_values('成绩',ascending=False)
        #
        scores = np.array(temp['成绩'])
        print("最大值:%d"%(scores.max()))
        print("最小值:%d"%(scores.min()))
        print("平均值:%.2f"%(scores.mean()))
        print("中位数:%d"%(np.median(scores)))
        num = temp.shape[0]   
        record = np.ones((num,))
        for i in range(1,num):
            if(scores[i-1]==scores[i]):
                record[i] = record[i-1]+1
            else:
                record[i] = 1 
        maxloc = np.argwhere(record==record.max())#所有众数的位置
        for i in scores[maxloc].reshape(maxloc.shape[0],).tolist():
            print("众数:%d"%i)# -*- coding: utf-8 -*-
    
