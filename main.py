#-*-coding:utf8;-*-
#qpy:console
#qpy:2

"""
one million RMB demo..

@Author: Tmn07
@Date: 2016-08-07
"""
import androidhelper
import time
droid = androidhelper.Android()

def dialogsetsinglechoiceitems():
    droid.dialogCreateAlert('要看目标还是记账？')
    droid.dialogSetSingleChoiceItems(['1. 看目标','2. 记账'])
    droid.dialogSetPositiveButtonText('确定')
    droid.dialogShow()
    # print(droid.dialogGetResponse())
    # print(droid.dialogGetSelectedItems())
    droid.dialogGetResponse()
    return droid.dialogGetSelectedItems()

def dialogcreateinput(problem):

    droid.dialogCreateInput(problem,'不能为空')

    droid.dialogSetPositiveButtonText('确定')

    droid.dialogShow()
    
    return droid.dialogGetResponse()


import pymongo

Conn = pymongo.MongoClient("127.0.0.1",27017)
try:
    Re = Conn.admin.authenticate("root","root")
    db = Conn.OneMillion
except Exception, e:
    # raise e
    print("passcode has been changed")
    exit()
    
choice = dialogsetsinglechoiceitems()

if choice[1][0]:
    result = dialogcreateinput("请输入金额")
    money = result[1]['value']

    result = dialogcreateinput("请输入说明")
    description = result[1]['value']
    
    try:
        db.record.insert({'money':float(money),"description":description,"name":"Tmn07","time":time.asctime(time.localtime(time.time())) })
    except Exception, e:
        print("输入错误")
    else:
        droid.makeToast("成功录入")

else:
    result = db.record.aggregate([{"$group":{"_id":"$name" ,"num":{"$sum":"$money"}}}])
    
    for i in result:
        if i['_id'] == "Tmn07":
            num = 1000000 - i['num']
        else:
            continue
    print("还差"+str(num))
    droid.makeToast("还差"+str(num))
    
