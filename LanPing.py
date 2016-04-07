import platform
import sys
import os
import time
from _thread import start_new_thread

active_ips = []
  
def get_os():
    os = platform.system()
    if os == "Windows":
        return "n"
    else:
        return "c"
    
def ping_ip(ip_str):
    cmd = ["ping", "-{op}".format(op=get_os()),
        "1", ip_str]
    output = os.popen(" ".join(cmd)).readlines()
      
    flag = False
    for line in list(output):
        if not line:
            continue
        if str(line).upper().find("TTL") >= 0:
            flag = True
            break
        
    if flag:
        print("ip: %s is ok ***" % ip_str)
        active_ips.append(ip_str)
    else:
        print("ip: %s no respond"% ip_str)
        
def find_ip(ip_prefix):
    for i in range(1, 256):
        ip = '%s.%s' % (ip_prefix, i)
        start_new_thread(ping_ip, (ip,))
        # thread.start_new_thread(ping_ip, (ip,))
        time.sleep(0.3)
  
if __name__ == "__main__":
    print("start time %s" % time.ctime())
    commandargs = sys.argv[1:]
    args = "".join(commandargs)  
      
    #ip_prefix = '.'.join(args.split('.')[:-1])
    ip_prefix = "192.168.1"
    find_ip(ip_prefix)
    print("end time %s" % time.ctime())
    print(active_ips)
