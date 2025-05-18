from flask import Flask,render_template,request,redirect
from db import database
app = Flask(__name__)

dbo = database()
@app.route('/')

def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/p',methods=['post'])

def perform_registeration():

    name = request.form.get('Name')
    email = request.form.get('email')
    password = request.form.get('password')
    response = dbo.insert(email,name,password)
    if response ==1:
       return render_template('login.html', message="Registered successfully.Kindly login")
    elif response == 0:
       return render_template('register.html', message="Already registered")
   
    
@app.route("/l",methods =['post'])

def perform_login():
    email =request.form.get('email')
    password = request.form.get('password')

    response = dbo.search(email,password)
    if response == 1:
        return redirect('/dashboard')
   
    elif response == 0:
        return render_template('login.html', message="password does not match")
    elif response == 2:
        return render_template('login.html', message="not registered")

# @app.route("/profile")

# def profile():
#    return render_template('profile.html')

# @app.route("/ner")

# def ner():
#     return render_template('ner.html')

# @app.route("/perform_ner",methods=['post'])    

# def perform_ner():
#     response = request.form.get('text')

#     return f"Received: {response}"

@app.route("/dashboard")

def dashboard():
    return render_template('dashboard.html')

app.run(port =5050 ,debug=True)