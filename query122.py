import requests
from datetime import date

query_url = 'http://bj.122.gov.cn/drv/yy/getKsdd'

def query():
    ss = requests.session()
    postdatas = {"startTime":"2016-05-20","endTime":"2016-06-03","kskm":2}
    reply = requests.post(query_url,postdatas,verify=False)
    print reply.status_code,reply.text

if __name__ == "__main__":
    query()