from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home():
  display = "Line is Null probably"
  try:
    with open('temp_history.txt') as f:
      lines = f.readlines()
      for line in lines:
        if line != "\n":
          display = line
  except:
    display = "Line is Null probably"
  return "<h1> "+display+" </h1>"
def run():
  app.run(host='0.0.0.0',port=8080)
  print("")
def keep_alive():
    t = Thread(target=run)
    print('---Server started---')
    t.start()
    print("")


