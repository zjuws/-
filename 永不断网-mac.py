import os,subprocess
      
def netOkorFail():  
    fnull = open(os.devnull, 'w')
    result=subprocess.call('ping -c 1 www.baidu.com',shell=True,stdout=fnull,stderr=fnull)
    if result:
        subprocess.call('node D:\www.cst.zju.edu.cn-cengwang-master\app.js',shell=True,stdout=fnull,stderr=fnull)
    else:
        print 'good'
    fnull.close()

netOkorFail()
