from requests import *

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
           'Cookie':'JSESSIONID=0A01D729FCB08817A9CD094A9C5A923C6E02B4CDFE; __NRF=452EB0C226EA6E52FCBD2E21EC1DDE92; _jc_save_toDate=2016-01-29; BIGipServerotn=701956362.64545.0000; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u6F2F%u6CB3%2CLON; _jc_save_fromDate=2016-04-07; _jc_save_wfdc_flag=dc'}
r = get('https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=2016-04-07&from_station=BJP&to_station=LON',headers=headers, verify=False)
print r.status_code
print r.request.headers['User-Agent']
print r.content