s = float(input('��������ߣ��ף���'))
y = float(input('���������أ������'))
n = input('������������䣺')
def qiwen():
    if n<10:
        print('��ͯ������')

    if n>=10 and n<60:
        mbi=y/(s*s)
        if mbi>24:
            print("����")
            return
        if mbi<18:
            print("����")
        else:
            print("����")
    if  n>=60:
        print('���˲�����')

qiwen()
        
