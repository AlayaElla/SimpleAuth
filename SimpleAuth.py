from flask import Flask, redirect, url_for, request
import datetime
import pytz
import hashlib

passwd = "HELLO"
app = Flask(__name__)

def compareToken(passwd,usr_token):
    nowtime = datetime.datetime.now(pytz.timezone('Asia/Shanghai'))
    nowtimeStr = nowtime.strftime('%Y-%m-%d %H:%M')
    pre_token = nowtimeStr+passwd
    token = hashlib.sha256(pre_token.encode('utf-8')).hexdigest()

    if(token == usr_token):
        return True
    else:
        return False

@app.route('/plantcare/',methods = ['POST'])
def plantcare_post():
   if request.method == 'POST':
        usr_token =  request.json["token"]

        if(compareToken(passwd,usr_token)):
            return "success"
        else:
            return "failed"

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000)