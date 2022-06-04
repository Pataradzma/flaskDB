from flask import Flask,request,render_template,url_for,redirect,session
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///group8.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class group8(db.Model):
    id = db.Column('student_id',db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    age = db.Column(db.Integer)
    uni = db.Column(db.String(100))


def __ini__(self,name,lastname,age,uni):
    self.name = name
    self.lastname = lastname
    self.age = age
    self.uni = uni

@app.route('/adduser',methods = ['POST','GET'])
def adduser():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['passwrod']
        lastname = request.form['lastname']
        age = request.form['age']
        uni = request.form['uni']
        user_infor = group8(name=name,lastname=lastname,uni=uni,age=age)
        db.session.add(user_infor)
        db.session.commit()
        return redirect(url_for('info'))

    return render_template('adduser.html')


@app.route('/info')
def info():
    return render_template('information.html',database = group8.query.all())

