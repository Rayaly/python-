s = float(input('请输入身高（米）：'))
y = float(input('请输入体重（公斤）：'))
n = input('请输入你的年龄：')
def qiwen():
    if n<10:
        print('儿童不参与')

    if n>=10 and n<60:
        mbi=y/(s*s)
        if mbi>24:
            print("超重")
            return
        if mbi<18:
            print("过轻")
        else:
            print("正常")
    if  n>=60:
        print('老人不参与')

qiwen()
        
