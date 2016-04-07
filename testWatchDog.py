# -*- coding:utf-8 -*-
'''
Created on 2016/3/12

@author: zxj
'''
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,\
                        format='%(asctime)s - %(message)s',\
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    ob = Observer()
    ob.schedule(event_handler, path, True)
    ob.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        ob.stop()
    ob.join()