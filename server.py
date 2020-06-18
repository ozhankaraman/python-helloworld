from flask import Flask, abort, Response
import sys
import os

PORT = 8080
#MESSAGE = "Hello World\n" + "BRANCH:" + os.environ['BRANCH'] + "\nVERSION:" + os.environ['VERSION'] + "\nGITCOMMIT:" + os.environ['GITCOMMIT'] + "\n"
MESSAGE = "Hello World\n<br><br>" + "BRANCH: " + os.environ['BRANCH'] + "\n<br>VERSION: " + os.environ['VERSION'] + "\n<br>GITCOMMIT: " + os.environ['GITCOMMIT'] + "\n<br>TAG: " + os.environ['TAG'] + "\n<br>ERROR_ENABLED: " + os.environ['ERROR'] + "\n<br>" + "\nHOSTNAME: " + os.environ['HOSTNAME'] + "\n<br>"
MESSAGE_MARS = "Hello Mars\n"

app = Flask(__name__)

counter = 0
@app.route("/")
def hello_world():
    global counter
    global MESSAGE
    counter += 1

#    if os.environ['VERSION'] == "3.2.22":
    if os.environ['ERROR'] == "yes":
        if (counter % 10) > 5:
            abort(500)

    MESSAGE2 = MESSAGE + "COUNTER: " + str(counter) + "\n<br>"
    return MESSAGE2.encode("utf-8")
        
    # if divmod(int(time.time()), 10)[1] <= 3:
    #     abort(500)
    # else:
    #     return MESSAGE.encode("utf-8")
    # return MESSAGE.encode("utf-8")

@app.route("/mars")
def hello_mars():
    return MESSAGE_MARS.encode("utf-8")

@app.route("/healtz")
def healtz():
    return "OK\n".encode("utf-8")

@app.route('/error')
def error():
    abort(500)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
