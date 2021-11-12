from flask import Flask, request
app = Flask(__name__)

@app.route("/login",methods = ["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username is not None and (username == "orapin") and password is not None and (password == "python"):
        return "Login Success."
    else:
        return "Login Fail!!!"
    
if __name__ == '__main__':
   app.run()