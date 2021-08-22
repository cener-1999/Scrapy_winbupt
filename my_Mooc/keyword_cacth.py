# -*-coding:utf-8-*-

import jieba.analyse
import re
from database.session import get_session
from database.createbales import Project_ifo

#TODO:制作themeTOP，用原生的词典，除去专业技术

class Keywords_Catch():

    def __init__(self):
        self.keywords={}
        self.makeDic()

    #初始内容存盘,主要为了测试
    def getFile(self):
        fp=open('allcontent.txt','w')
        session = get_session()
        results = session.query(Project_ifo).all()
        for result in results:
            str=(result.procontent)
            str=re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", (str))
            self.catchWord2(str)
            fp.write(str)

    #从DB中取原生text，进行预处理（去除无用符号）
    def getDate(self):
        session = get_session()
        results = session.query(Project_ifo).all()
        for result in results:
            str=(result.achievements)
            str=re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", (str))
            self.catchWord2(str)
        self.findMax()

        for i in range(len(self.top)):
            print(self.top[i])


    #方法一：清华词库加自己的stop
    def catchWord(self,str):
        words=jieba.cut(str)
        jieba.load_userdict("THUOCL_it.txt")
        #制作词典
        for word in words:
            if word not in self.stop_words:
                if( word in self.keywords):
                    self.keywords[word]+=1
                else:
                    self.keywords[word]=1

    #方法二：自带的屏蔽词
    def catchWord2(self,str):
        words=jieba.analyse.extract_tags(str)
        #制作词典
        for word in words:
            if( word in self.keywords):
                self.keywords[word]+=1
            else:
                self.keywords[word]=1

    #方法三：两个都是自己做的
    def catchWord3(self,str):
        words=jieba.cut(str)
        jieba.load_userdict("technology_dic.txt")
        #制作词典
        for word in words:
            if word not in self.stop_words:
                if( word in self.keywords):
                    self.keywords[word]+=1
                else:
                    self.keywords[word]=1

    def findMax(self):
        #把字典转为有序词典
        word = list(self.keywords.keys())
        times = list(self.keywords.values())
        self.top = []
        for i in range(len(self.keywords)):
            self.top.append((times[i],word[i]))
        self.top.sort(reverse=True)
        #对应技术词典,截取前十五的高频
        # self.top15 = []
        # for i in range (len(self.top)):
        #     if self.top[i][1] in self.tec_words:
        #         if(len(self.top15)<15):
        #             self.top15.append(self.top[i])
        #对应theme,去除专业技术
        # self.top15 = []
        # for i in range (len(self.top)):
        #     if (self.top[i][1] not in self.tec_words) and (self.top[i][1] not in self.not_theme):
        #         if(len(self.top15)<20):
        #             self.top15.append(self.top[i])
        #             print(self.top[i])
        # 对应要求
        # self.top15 = []
        # for i in range (len(self.top)):
        #     if (self.top[i][1] not in self.not_req):
        #         if(len(self.top15)<20):
        #             self.top15.append(self.top[i])
        #             print(self.top[i])

        #对应成果形式
        self.top15 = []
        for i in range (len(self.top)):
            if (self.top[i][1] not in self.not_ach):
                if(len(self.top15)<10):
                    self.top15.append(self.top[i])
                    print(self.top[i])
        #self.storeDate()

    #制作停用词和专业词词典
    def makeDic(self):
        print("!!!!!")
        stopwords_file = "ciku/stopwords.txt"
        stop_f = open(stopwords_file, "r", encoding='utf-8')
        #停用词词表
        self.stop_words = list()
        for line in stop_f.readlines():
            line = line.strip()
            if not len(line):
                continue
            self.stop_words.append(line)
        #技术词表
        stopwords_file = "ciku/technology_dic.txt"
        tec_f = open(stopwords_file, "r", encoding='utf-8')
        self.tec_words=[]
        for line in tec_f.readlines():
            line = line.strip()
            if not len(line):
                continue
            self.tec_words.append(line)

        #非主题词表
        stopwords_file = "ciku/not_theme.txt"
        tec_f = open(stopwords_file, "r", encoding='utf-8')
        self.not_theme=[]
        for line in tec_f.readlines():
            line = line.strip()
            if not len(line):
                continue
            self.not_theme.append(line)

        # 非要求词表
        stopwords_file = "ciku/not_req.txt"
        tec_f = open(stopwords_file, "r", encoding='utf-8')
        self.not_req = []
        for line in tec_f.readlines():
            line = line.strip()
            if not len(line):
                continue
            self.not_req.append(line)
        # 非要求词表
        stopwords_file = "ciku/not_req.txt"
        tec_f = open(stopwords_file, "r", encoding='utf-8')
        self.not_req = []
        for line in tec_f.readlines():
            line = line.strip()
            if not len(line):
                continue
            self.not_req.append(line)
        # 非成果词表
        stopwords_file = "ciku/not_ach.txt"
        tec_f = open(stopwords_file, "r", encoding='utf-8')
        self.not_ach = []
        for line in tec_f.readlines():
            line = line.strip()
            if not len(line):
                continue
            self.not_ach.append(line)

    #存top15的数据给后端，以txt的形式
    #记得改文件名
    def storeDate(self):
        filename="results/ach_top10.txt"
        result_f = open(filename, "w", encoding='utf-8')
        for data in self.top15:
            print(data)
            result_f.write(str(data[0])+' '+data[1]+'\n')


test=Keywords_Catch()
test.getDate()