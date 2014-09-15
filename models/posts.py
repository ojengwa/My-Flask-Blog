from sqlite3 import connect
from time import ctime

def save(author, pid, title, content):
    con = connect('Models/blog.db')
    c = con.cursor()
    time = str(ctime())
    c.execute("INSERT INTO posts VALUES ('%s', '%s', '%s', '%s', '%s')" % (author, pid, title, content, time))
    con.commit()

    con.close()

    return True

def delete(uid, pid):
    con = connect('Models/blog.db')
    c = con.cursor()

    c.execute("DELETE FROM blog WHERE id = '%s' AND uid = '%s')" % (author, pid, title))
    con.commit()

    con.close()
    return True

def fetchAll(count = 100):
    con = connect('Models/blog.db')
    c = con.cursor()
    c.execute("SELECT * FROM posts LIMIT %d" % count)
    posts  = c.fetchall()
    return posts
    
def fetchSingle(id):
    f = 'Models/blog.db'
    con = connect(f)
    c = con.cursor()
    c.execute("SELECT * FROM posts WHERE pid = '%s'" % id)
    post = c.fetchone()
    comments = fetchComments(id)
    return post, comments
    
def fetchComments(id):
    con = connect('Models/blog.db')
    c = con.cursor()
    c.execute("SELECT * FROM comments WHERE postid = '%s'" % id)
    comments  = c.fetchall()
    if comments == None:
        return False
    return comments
    
def addComment(uid, pid, msg):
    con = connect('Models/blog.db')
    c = con.cursor()
    time = str(ctime())
    c.execute("INSERT INTO comments VALUES ('%s', '%s', '%s', '%s')" % (uid, pid, msg, time))
    con.commit()
    con.close()
    return True