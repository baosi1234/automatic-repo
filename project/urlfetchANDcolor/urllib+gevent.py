# python day 18
# author zach.wang
# -*- coding:utf-8 -*-
import gevent
from gevent import monkey
from urllib.request import urlopen

#防止IO阻塞
monkey.patch_all()

dir = ""
def trapurl(url):
    res = urlopen(url)
    data = res.read()
    webname = "".join(("".join(url.split("//")[1:])).split("/")[:1])
    #需要使用二进制写入，否则无法换行
    with open(dir+webname+".html","wb") as f:
        f.write(data)
    gevent.sleep(1)
    print("{} fetch success!".format(webname))


def urlretrieve(url):
    from urllib import request
    webname = "".join(("".join(url.split("//")[1:])).split("/")[:1])
    request.urlretrieve(url,dir+webname+'.html')
    #清除使用urlopen或urlretrieve后产生的缓存文件
    request.urlcleanup()
    gevent.sleep(1)
    print("{} fetch success!".format(webname))

#FIXME 使用协成将无效
'''
def abc(a,b,c):
    '''''
    a: num
    b: size
    c: total
    '''
    process = 100.0*a*b/c
    if process > 100:
        process = 100
    print('%.2f%%' %process)

url = 'https://docs.python.org/3.0/library/urllib.robotparser.html'
request.urlretrieve(url,'aaa.html',abc)

'''

if __name__ == '__main__':
    choice = trapurl
else:
    choice = urlretrieve

gevent.joinall([gevent.spawn(choice,"https://www.python.org/"),
               gevent.spawn(choice,"http://www.qq.com/"),])