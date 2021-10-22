#! C:\Users\pride\AppData\Local\Programs\Python\Python38\python.exe
print("content-type:text/html; charset=UTF-8\n")
print()

import cgi
from os import listdir

form = cgi.FieldStorage()

if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId,'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello Web'

data_li = listdir('data')

listStr=''
for item in data_li:
    listStr = listStr + '<li><a href = "index.py?id={name}">{name}</a></li>'.format(name=item)


print('''
<!doctype html>
<html>
<head>
    <title>WEB1 - Welcome</title>
    <meta charset="utf-8">
</head>
<body>
    <h1><a href="index.py">WEB</a></h1>
    <ol>
    {data_list}
    </ol>
    <a href="create.py">create</a>
    <h2>{title}</h2>
    <p>{desc}</p>
</body>
</html>
'''
.format(title=pageId, desc = description, data_list = listStr))