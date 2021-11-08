import os

def getList():
    data_li = os.listdir('data')
    listStr=''

    for item in data_li:
        listStr = listStr + '<li><a href = "index.py?id={name}">{name}</a></li>'.format(name=item)
    return listStr

