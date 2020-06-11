from flask import Flask, abort, Response
import sys
import os

PORT = 8080
#MESSAGE = "Hello World\n" + "BRANCH:" + os.environ['BRANCH'] + "\nVERSION:" + os.environ['VERSION'] + "\nGITCOMMIT:" + os.environ['GITCOMMIT'] + "\n"
MESSAGE = "Hello World\n" + "BRANCH " + os.environ['BRANCH'] + "\nVERSION " + os.environ['VERSION'] + "\nGITCOMMIT " + os.environ['GITCOMMIT'] + "\nTAG " + os.environ['TAG'] + "\n"
MESSAGE2 = "Hello Africa\n"

#print(sys.argv)
#for param in os.environ.keys():
#    print ("%20s %s" % (param,os.environ[param]))

app = Flask(__name__)

@app.route("/")
def hello_world():
    return MESSAGE.encode("utf-8")

@app.route("/africa")
def hello_africa():
    return MESSAGE2.encode("utf-8")

@app.route("/healtz")
def healtz():
    return "OK\n".encode("utf-8")

@app.route('/error')
def error():
    abort(500)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
