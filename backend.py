from flask import Flask, render_template, request
from AES import *
import time
app = Flask(__name__, static_folder="static")
@app.route('/')
def hello_world():
   return render_template('webinterface.html')

@app.route('/encrypt', methods = ['POST'])
def Aencrypt():
   info = ("state", "key", "IV", "cipher", "hexain", "hexakey", "hexaout", "hexaIV", "b64", "mode")
   d = {i : request.form.get(i, "False") for i in info}
   rtime = time.process_time() 
   e = encrypt(**d)
   rtime = str((time.process_time() - rtime)*1000) + "ms"
   return {"cypherkey": e, "time": rtime}

@app.route('/decrypt', methods = ['POST'])
def Adecrypt():
   info = ("state", "key", "IV", "cipher", "hexain", "hexakey", "hexaout", "hexaIV", "b64", "mode")
   d = {i : request.form.get(i, "False") for i in info}  
   rtime = time.process_time()
   e = decrypt(**d)
   rtime = str((time.process_time() - rtime)*1000) + "ms"
   return {"cypherkey": e, "time": rtime}

if __name__ == '__main__':
   app.run()