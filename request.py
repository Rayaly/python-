#coding=gbk
import requests

daima = input('请输入股票代码：')
print(daima)
def getStockPrice(daima):
    ret = requests.get(f'http://hq.sinajs.cn/list={daima}',headers ={'Referer':'http://finace.sina.com.cn'})
    # 返回的内容在消息体中，通过text属性获取
    a = ret.text
    a = a.split(',')
    print(a)
    print('股票今日开盘价为：',a[1])
getStockPrice(daima)
