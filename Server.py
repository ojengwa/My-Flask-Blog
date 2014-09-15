from flask import Flask, redirect, session, url_for, request, render_template, abort
from controller import *
from os import urandom

app = Flask(__name__)
app.secret_key = urandom(24)

#Router and view for posting articles
@app.route('/post.do/<id>', methods = ['GET', 'POST'])
def post(id=None):
    params = dict()
    params['title'] = 'New Article'
    if not session['valid']:
        return redirect( url_for('index'))
    if request.method == 'GET':
        return render_template('post.html',  param = params)
    else:
        req = request.form
        result = postOne(req)
        if result:
            params['msg'] = 'Your post was successful'
            return render_template('post.html', param = params)
        else:
            params['msg'] = 'Could not post your article'
            return render_template('post.html', param = params)
            
#router and view for the contact page, removed
@app.route('/contact.do', methods = ['GET', 'POST'])
def contact():
    params = dict()
    params['title'] = 'Contact Us'
    return render_template('contact.html', param = params)

#router and view for displaying a single post    
@app.route('/single/<pid>', methods = ['GET', 'POST'])
def single(pid):
    if pid == None:
        abort(404)
    if request.method == 'GET':
        result, name, comm = singlePost(pid)
        if result == False:
            abort(404)
        params = dict()
        params['title'] = result[2]
        params['post'] = result
        params['author'] = name
        params['comments'] = comm
        return render_template('single.html', param = params)
    else:
        req = request.form
        result = addComments(pid, req)
        return redirect(request.path)

#router and glue for general authentications        
@app.route('/auth', methods = ['GET', 'POST'])
def auth():
    if request.method == 'GET':
        abort(404)
    req = request.form
    result = authUser(req)
    if result[2] == True:
        print result[2]
        session['valid'] = result[2]
        session['name'] = result[1]
        session['id'] = result[0]
    else:
        session['err'] = result[1]
    return redirect(req['path'])

#Just logout    
@app.route('/logout')
def logout():
    session.pop('id', None)
    session.pop('valid', None)
    session.pop('name', None)
    session.pop('err', None)
    return redirect(url_for('index'))

#Homepage views plus routes
@app.route('/', methods = ['GET', 'POST'])
@app.route('/index.do', methods = ['GET', 'POST'])
def index():
    params = dict()
    params['title'] = 'Welcome'
    result = recents(10)
    params['posts'] = result
    return render_template('index.html', param = params)

#for 404s and enforcing permissions in some places
@app.errorhandler(404)
def err(err):
    params = dict()
    params['title'] = '404 Page'
    return render_template('err.html', param = params), 404
    pass
#Bootstarter
if __name__ == "__main__":
    print "Server running"
    app.run(debug = True)