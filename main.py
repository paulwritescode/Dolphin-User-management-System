from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URi'] = "sqlite:///ums.sqlite"
app.config["SECRET_KEY"] = ""
db = SQLAlchemy(app)

# User class
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fname = db.C


# MAIN INDEX LOGIN
@app.route("/")
def index():
    return render_template('indexMain.html')

# ADMIN LOGIN
@app.route("/admin/")
def adminIndex():
    return render_template('admin/index.html', title ="Admin Login")

# User Area
# login
@app.route("/user/")
def userIndex():
    return render_template('User/index.html', title ="User Login")

# register
@app.route("/user/signup")
def userSignUp():
    return render_template('User/signup.html', title ="User signup")

if __name__=="__main__":
    app.run(debug=True)
