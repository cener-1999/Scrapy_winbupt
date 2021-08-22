# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from my_Mooc.database.opreation import Opreation


class MyMoocPipeline(object):
    def process_item(self, item, spider):

        # test = Opreation()
        # id =int((item['id'][5:]))
        # name = item['name']
        # department = item['department'][5:]
        # date = item['date'][5:]
        # procontent =item['procontent']
        # goal = item['goal']
        # achievements =item['achievements']
        # requests = item['requests']
        # test.ifo_insert(id,name, department, date,procontent,goal,achievements,requests)
        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        # print(id,department,date)

        test=Opreation()
        name=item['name']
        department=item['department']
        date=item['date']
        test.table_insert(name,department,date)

        return item
