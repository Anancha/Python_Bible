from flask import Flask
app = Flask(__name__)

@app.route("/echo/<uname>")
def echo_name(uname):
   return "Hello %s!" % uname

@app.route("/echofull/<fname>/<lname>")
def echo_fullname(fname,lname):
    fullname = fname+" "+lname
    return "Hello %s!" % fullname

if __name__ == '__main__':
   app.run()