# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql

class SpiderPipeline:
    def open_spider(self, spider):
        self.conn = pymysql.connect(host='localhost',user='root',password='XXXXX')
        self.cursor = self.conn.cursor()
        pymysql.charset='gbk'
        #self.article = open('./doubanmovie.csv', 'a', encoding='utf-8')

    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
    def process_item(self, item, spider):
        name = item['name']
        category = item['category']
        show_time = item['show_time']
        value = (name, category, show_time)
        self.values.append(value)
        try:
            self.cur.execute("insert into scrapy(name, category, show_time) values(%s,%s,%s)" % (name, category, show_time))
            self.conn.commit()
        except Exception as err:
            self.rollback()
            print(err)
        #output = f'|{name}|\t|{category}|\t|{show_time}|\n\n'
        #self.article.write(output)

        return item

    def close_spider(self, spider):
        self.conn.close()