# -*-coding:utf-8-*-
from sqlalchemy import create_engine
from my_Mooc.database.session import get_session
from my_Mooc.database.createbales import *

class Opreation():
    def table_insert(self,name,department,date):
        # 取得session对象
        session = get_session()
        # 创建 Course类实例
        project_obj = Projects(name=name,department=department, date=date)
        # 添加对象
        session.add(project_obj)
        # 事务提交
        session.commit()

    def ifo_insert(self, id, name, department, date, procontent, goal, achievements, requests):
        # 取得session对象
        session = get_session()
        # 创建 Course类实例
        project_obj = Project_ifo(id=id, name=name, department=department, date=date, procontent=procontent, goal=goal,
                                  achievements=achievements, requests=requests)
        # 添加对象
        session.add(project_obj)
        # 事务提交
        session.commit()


#test=Opreation()
#test.ifo_insert(id=2, name='name', department='cs', date='010', procontent='sadhlhwuh kjfwefhoiweuf', goal='sar wrajsdddddddddddddddddhiawufhihcwuihhfalewufhlefhul hwhfaeejfemniuytrertyuio', achievements='sar wrajsdddddddddddddddddhiawufhihcwuihhfalewufhlefhul hwhfaeejfemniuytrertyuio', requests='sar wrajsdddddddddddddddddhiawufhihcwuihhfalewufhlefhul hwhfaeejfemniuytrertyuio')
#test_insert.table_insert('insert_test','software','2021/08/22')