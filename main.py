from flask import Flask, flash, redirect, render_template, request
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ums.sqlite"
app.config["SECRET_KEY"] = '6b32023662dbe91f2c19de4c'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)



if __name__=="__main__":
    db.create_all()
    app.run(debug=True)


# user class
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(255), nullable = False)
    lname = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(255), nullable = False)
    username = db.Column(db.String(255), nullable = False)
    edu = db.Column(db.String(255), nullable = False)
    password = db.Column(db.String(255), nullable = False)
    status = db.Column(db.Integer, default = 0, nullable = False)

    def __repr__(self):
        return f'User("{self.id}","{self.fname}","{self.lname}","{self.email}","{self.edu}","{self.username}","{self.status}",)'



# first landing page
@app.route("/")
def index():
    return render_template('indexMain.html')
# Admin login
@app.route("/admin/")
def adminIndex():
    return render_template('admin/index.html', title ="Admin Login")

# User Area
# login
@app.route("/user/")
def userIndex():
    return render_template('User/index.html', title ="User Login")
# register
@app.route("/user/signup", methods = ['POST', 'GET'])
def userSignUp():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        username = request.form.get('username')
        edu = request.form.get('edu')
        password = request.form.get('password')

        # check that all the fields are filled
        if fname == "" or lname == "" or lname == "" or email == "" or password == "" or username == "" or edu == "":
            flash('Please fill all the fields', 'danger')
            return redirect('/user/signup')
        else:
            hash_password = bcrypt.generate_password_hash(password, 10)
            user = User(fname = fname, lname = lname, email = email, password = hash_password, edu = edu, username = username)
            db.session.add(user)
            db.session.commit()
            flash('Acount created successfully Admin will approve your account in 10 to 30 min', 'success')
            return redirect('/user/')

    else:
        return render_template('User/signup.html', title ="User signup")



