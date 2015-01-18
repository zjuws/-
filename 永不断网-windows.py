import os,subprocess
import time      
def netOkorFail():  
    fnull = open(os.devnull, 'w')
    result=subprocess.call('ping www.baidu.com',shell=True,stdout=fnull,stderr=fnull)
    if result:
        command = 'node D:\\www.cst.zju.edu.cn-cengwang-master\\app.js'  
        os.system(command)
    else:       
        print 'good'
    fnull.close()
while 1:
    netOkorFail()
    time.sleep(600)
