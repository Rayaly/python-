#coding=gbk
import requests

daima = input('�������Ʊ���룺')
print(daima)
def getStockPrice(daima):
    ret = requests.get(f'http://hq.sinajs.cn/list={daima}',headers ={'Referer':'http://finace.sina.com.cn'})
    # ���ص���������Ϣ���У�ͨ��text���Ի�ȡ
    a = ret.text
    a = a.split(',')
    print(a)
    print('��Ʊ���տ��̼�Ϊ��',a[1])
getStockPrice(daima)
