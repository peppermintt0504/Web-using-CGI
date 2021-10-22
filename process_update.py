#! C:\Users\pride\AppData\Local\Programs\Python\Python38\python.exe

import cgi, os

form = cgi.FieldStorage()

pageId = form["pageId"].value
title = form["title"].value
desc = form["description"].value


opened_file = open('data/'+ pageId,"w")
opened_file.write(desc)
opened_file.close()

os.rename('data/'+pageId, 'data/'+title)



#Redirection
print("Location: index.py?id="+title)
print()
