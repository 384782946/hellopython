# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from lxml import etree
import codecs
import json
import requests
from datetime import date,datetime
import time

query_url = "https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=%s&from_station=%s&to_station=%s"
query_by_train_url = "https://kyfw.12306.cn/otn/czxx/queryByTrainNo?train_no=%s&from_station_telecode=%s&to_station_telecode=%s&depart_date=%s"
citys = {"北京": "BJP",
         "保定": "BDP",
         "石家庄": "VVP",
         "邢台": "XTP",
         "邯郸": "HDP",
         "安阳": "AYF",
         "鹤壁": "HBF",
         "新乡": "XXF",
         "郑州": "ZZF",
         "许昌": "XCF",
         "漯河": "LON",
         "驻马店":"ZDN",
         "信阳":"XUN"}

def getCityCode(cityName):
    code = citys.get(cityName, None)
    if code is None:
        uName = cityName.decode('utf-8')
        uName = uName[0:-1]
        code = citys.get(uName.encode('utf-8'),None)
    return code

def toInt(string,defualt = None):
    try:
        ret = int(string)
    except:
        ret = defualt
    return ret

class Ticket():
    start_code = ""
    end_code = ""
    start_station_name = ""
    end_station_name = ""
    start_time = ""
    arrive_time = ""
    day_difference = 0
    gr_num = 0
    rw_num = 0
    rz_num = 0
    tz_num = 0
    wz_num = 0
    yw_num = 0
    yz_num = 0
    ze_num = 0
    zy_num = 0
    swz_num = 0

    def isValid(self):
        return (self.gr_num+self.rw_num+self.rz_num+self.tz_num+self.wz_num+self.yw_num+self.yz_num+self.ze_num+self.zy_num+self.swz_num) > 0

class Train():
    train_no = ""
    start_train_date = ""
    start_station_telecode = ""
    end_station_telecode = ""
    train_class_name = ""
    stations = []
    station_train_code = ""
    tickets = {}

    def __str__(self):
        return "<%s>:\n类型:%s\n始发站:%s\n终点站:%s\n时间:%s-%s\n途经:%s\n高级软卧:%d\n软卧:%d\n软座:%d\n特等座:%d\n无座:%d\n硬卧:%d\n硬座:%d\n二等座:%d\n一等座:%d\n商务座:%d" \
               % (self.station_train_code,self.train_class_name,self.start_station_name,self.end_station_name,self.start_time,self.arrive_time,','.join(self.stations),self.gr_num,self.rw_num,self.rz_num,self.tz_num,self.wz_num,self.yw_num,self.yz_num,self.ze_num,self.zy_num,self.swz_num)

    def isValid(self):
        for t in self.tickets:
            if t.isValid():
                return True
        return False

class Order():
    start_station = ""
    to_station = ""
    date = ""
    trains = []
    valid_trains = []
    stations = []

    def __init__(self,ss,ts,dt):
        self.start_station = ss
        self.to_station = ts
        self.date = dt

    def isValid(self,train):
        return train.isValid()

    def addTrain(self,train):
        self.trains.append(train)
        if self.isValid(train):
            self.valid_trains.append(train)

def query(dateStr,fromStr,toStr):
    url = query_url % (dateStr,fromStr,toStr)
    ret = requests.get(url, verify=False)
    if ret.status_code == 200:
        return ret.text
    else:
        return None

def queryByTrain(trainNo,dateStr,fromStr,toStr):
    url = query_by_train_url % (trainNo,fromStr,toStr,dateStr)
    ret = requests.get(url, verify=False)
    if ret.status_code == 200:
        return ret.text
    else:
        return None

def run(order):
    fromStation = getCityCode(order.start_station)
    toStation = citys.get(order.to_station,None)
    dateStr = order.date
    if fromStation and toStation:
        str = query(dateStr,fromStation,toStation)
        print str
        datas = json.loads(str.encode('utf-8'))
        if datas is None:
            return
        lists = datas['data']['datas']

        for item in lists:
            train = Train()
            train.train_no = item['train_no'].encode('utf-8')
            train.start_station_telecode = item['start_station_telecode'].encode('utf-8')
            train.end_station_telecode = item['end_station_telecode'].encode('utf-8')
            train.start_train_date = item['start_train_date'].encode('utf-8')
            train.station_train_code = item['station_train_code'].encode('utf-8')

            ticket = Ticket()
            ticket.start_code = fromStation
            ticket.end_code = toStation
            ticket.start_station_name = item['start_station_name'].encode('utf-8')
            ticket.end_station_name = item['end_station_name'].encode('utf-8')
            ticket.start_time = item['start_time'].encode('utf-8')
            ticket.arrive_time = item['arrive_time'].encode('utf-8')
            ticket.day_difference = toInt(item['day_difference'],0)
            ticket.gr_num = toInt(item['gr_num'],0)
            ticket.rw_num = toInt(item['rw_num'],0)
            ticket.rz_num = toInt(item['rz_num'],0)
            ticket.tz_num = toInt(item['tz_num'],0)
            ticket.wz_num = toInt(item['wz_num'],0)
            ticket.yw_num = toInt(item['yw_num'],0)
            ticket.yz_num = toInt(item['yz_num'],0)
            ticket.ze_num = toInt(item['ze_num'],0)
            ticket.zy_num = toInt(item['zy_num'],0)
            ticket.swz_num = toInt(item['swz_num'],0)

            key = "%s-%s" % (fromStation,toStation)
            train.tickets[key] = ticket

            dateStr = datetime.strptime(train.start_train_date,"%Y%m%d").strftime("%Y-%m-%d")
            qbtStr = queryByTrain(train.train_no,dateStr,train.start_station_telecode,train.end_station_telecode)
            trainInfo = json.loads(qbtStr)
            train.train_class_name = trainInfo['data']['data'][0]['train_class_name'].encode('utf-8')
            for s in trainInfo['data']['data']:
                train.stations.append(s['station_name'].encode('utf-8'))
            order.addTrain(train)
            print train

        if len(order.valid_trains) >0:#有票可买

            return

if __name__ == "__main__":
    run()