#! C:\Users\pride\AppData\Local\Programs\Python\Python38\python.exe

import cgi

form = cgi.FieldStorage()

title = form["title"].value
desc = form["description"].value


opened_file = open('data/'+title,"w")
opened_file.write(desc)

#Redirection
print("Location: index.py?id="+title)
print()
