from flask import Flask, render_template

app=Flask(__name__)

# __________________________MAIN INDEX LOGIN
@app.route("/")
def index():
    return render_template('indexMain.html')


# ____________________________________ADMIN LOGIN
@app.route("/admin/")
def adminIndex():
    return render_template('admin/index.html', title ="Admin Login")


# _____________________User Area_____________________________
@app.route("/user/")
def userIndex():
    return render_template('User/index.html', title ="User Login")




if __name__=="__main__":
    app.run(debug=True)
