import sqlite3

con = sqlite3.connect("blog.db")

c = con.cursor()

c.execute('''CREATE TABLE users
            (id text, fname text, lname text, email text, password text, online integer)''')
con.commit()
c.execute('''CREATE TABLE posts
            (uid text, pid text, title text, content text, date text)''')
con.commit()
c.execute('''CREATE TABLE comments
            (uid text, postid text, comment text, date text)''')
con.commit()

con.close()
