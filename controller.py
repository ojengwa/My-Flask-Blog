"""
Controller module;
Contain functions that acts as glue between the models and their respective glues
You must import this module to access member functions from your code, except your are daft
@TODO implement the contact form
"""

from models import users, posts, comments
from time import ctime

def recents(max):
    temp = posts.fetchAll(max)
    if len(temp) == 0:
        return False
    else:
        return temp
    
def postOne(form):
    title = form['title']
    author = form['uid']
    time = str(ctime())
    pid = str(hash(author + time))
    content = form['content']
    return posts.save(author, pid, title, content)
    
def authUser(arr):
    user = users.Users()
    if arr.has_key('fname'):
        fname = arr['fname']
        lname = arr['lname']
        email = arr['user']
        password = arr['pass']

        email = email.strip()
        password = password.strip()

        uid, name, true = user.signup(fname, lname, email, password)
        return uid, name, true
    else:
        email = arr['user']
        password = arr['pass']

        email = email.strip()
        password = password.strip()

        uid, name, true = user.login(email, password)
        return uid, name, true

def addComments(pid, form):
    uid = form['uid']
    pid = pid
    comment = form['message']
    return posts.addComment(uid, pid, comment)

def contact():
    pass
    
def singlePost(id):
    temp, comm = posts.fetchSingle(id)
    if temp == None:
        return False
    else:
        user = users.Users()
        name = user.getUser(temp[0])
        comments = []
        for row in comm:
            comments.append([user.getUser(row[0]), row])
        return temp, name, comments
