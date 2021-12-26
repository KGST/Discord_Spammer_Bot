#KEEP THE BOT RUNNING BY MAKING A WEBSITE AND USING A THIRD PARTY (ie Uptime robot) TO PING IT EVERY ONCE IN A WHILE 
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is currently running"

def run():
  app.run(host='0.0.0.0',port=8080)

def keepAlive():
    threadRun = Thread(target=run)
    threadRun.start()
