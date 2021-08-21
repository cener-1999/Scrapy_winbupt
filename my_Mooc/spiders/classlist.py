# -*-coding:utf-8-*-
from scrapy import Request
from scrapy import Spider
from my_Mooc.items import *

class Mooc_class_list(Spider):
    name='project_list'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    start_urls=['https://win.bupt.edu.cn/project.do?next=collectlist']

    def start_requests(self):
        url='https://win.bupt.edu.cn/project.do?next=collectlist'
        yield Request(url,headers=self.headers)

    def parse(self, response):
        filename="project_list.html"
        open(filename,'wb+').write(response.body)

        item=MyMoocItem()
        classes = response.xpath('//*[@id="posts"]/div/div')
        for the_class in classes:
            item['name']=the_class.xpath(
                './div/div[1]/p/a/text()').extract_first()
            item['department']=the_class.xpath(
                './div/div[1]/p/span[1]/text()'
            ).extract_first()
            item['date']=the_class.xpath(
                './div/ul/li/text()'
            ).extract_first()
            yield item

        next_page=1
        while next_page <124:
            next_page += 1
            next_url = 'https://win.bupt.edu.cn/project.do?next=collectlist&p=' + str(next_page)
            yield Request(next_url)

class Project_ifo(Spider):
    name = 'project_ifo'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    start_urls = ['https://win.bupt.edu.cn/project.do?next=collectproject&id=1']

    def start_requests(self):
        url = 'https://win.bupt.edu.cn/project.do?next=collectproject&id=13'
        yield Request(url, headers=self.headers)

    def parse(self, response):

        item =InfoItem()
        item['name'] = response.xpath('//*[@id="content"]/div/div[1]/div/div/div[1]/h2/text()').extract_first()
        item['id']=response.xpath('//*[@id="content"]/div/div[2]/div/div[1]/div[1]/text()').extract_first()
        item['department'] = response.xpath('//*[@id="content"]/div/div[2]/div/div[1]/div[4]/text()').extract_first()
        item['date'] = response.xpath('//*[@id="content"]/div/div[2]/div/div[1]/div[3]/text()').extract_first()
        item['procontent'] = response.xpath('//*[@id="content"]/div/div[1]/div/div/div[2]/blockquote[1]/text()').extract_first()
        item['goal'] = response.xpath(
            '//*[@id="content"]/div/div[1]/div/div/div[2]/blockquote[2]/text()').extract_first()
        item['achievements'] = response.xpath(
            '//*[@id="content"]/div/div[1]/div/div/div[2]/blockquote[3]/text()').extract_first()
        item['requests'] = response.xpath(
            '//*[@id="content"]/div/div[1]/div/div/div[2]/blockquote[4]/text()').extract_first()
        yield item

        next_page = 1
        while next_page <2223:
            next_page += 1
            next_url = 'https://win.bupt.edu.cn/project.do?next=collectproject&id=' + str(next_page)
            yield Request(next_url)