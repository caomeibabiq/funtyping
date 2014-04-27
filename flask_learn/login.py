#coding:utf8
from flask import Flask,url_for,request
from flask import render_template
app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error="log result"	
    if request.method == 'POST':
        if len(request.form['username'])<8 or len(request.form['password'])<8:
            error = "username or password is invalid"
        else:
            error = 'login ok'
    
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)



