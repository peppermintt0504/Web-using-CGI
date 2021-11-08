#! C:\Users\pride\AppData\Local\Programs\Python\Python38\python.exe
print("content-type:text/html; charset=UTF-8\n")
print()

import cgi, view
from os import listdir

form = cgi.FieldStorage()

if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId,'r').read()
    update_link = '<a href="update.py?id={name}">update</a>'.format(name = pageId)
    delete_action = '''
        <form action = "process_delete.py" method="post">
            <input type = "hidden" name = "pageId" value = "{}">
            <input type = "submit" value="delete">
        </form>

    '''.format(pageId)
else:
    pageId = 'Welcome'
    description = 'Hello Web'
    update_link = ''
    delete_action =''


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
    {update_link}
    {delete_action}
    <h2>{title}</h2>
    <p>{desc}</p>
</body>
</html>
'''
.format(
title=pageId,
desc = description,
data_list = view.getList(),
update_link = update_link,
delete_action = delete_action))