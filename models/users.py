"""The User's model, will create and authenticate user accounts"""
from os import getcwd, sep
from sqlite3 import connect

class Users:
    def signup(self, fname, lname, email, password):
        temp = ""
        self.fname = fname
        self.lname = lname
        self.email = email
        self.id = hash(email)
        self.password = hash(password)
        f = "Models/blog.db"
        con = connect(f)
        c = con.cursor()
        c.execute("SELECT * FROM users WHERE email= '%s' " % self.email) 
        if len(c.fetchall()) == 0:
            c.execute("INSERT INTO users VALUES ('%s', '%s', '%s', '%s', '%s', 1)" % (str(self.id), self.fname, self.lname, self.email, str(self.password)))
            con.commit()
            con.close()
            return self.id, self.fname + " " + self.lname, True
        else:
            con.close()
            return "Error", "Email already registered", False
       

    def login(self, email, password):
        f = "Models/blog.db"
        self.password = str(hash(password.strip()))
        self.email = email.strip()
        con = connect(f)
        c = con.cursor()
        c.execute("SELECT * FROM users WHERE email= '%s' AND password='%s'" % (self.email, self.password))
        user = c.fetchall()
        if len(user) == 0:
            con.close()
            return "Error", "You are not registered", False
        else:
            c.execute("UPDATE users SET online= %d WHERE email='%s'" % (1, email))
            con.commit()
        return user[0][0], user[0][1] + " " + user[0][2], True

    def getUser(self, uid):
        self.uid = uid
        f = "Models/blog.db"
        con = connect(f)
        c = con.cursor()
        c.execute("SELECT fname, lname FROM users WHERE id = '%s'" % self.uid)
        user = c.fetchone()
        if len(user) == 0:
            return "Not Found"
        else:
            
            return user[0] + " " + user[1]
