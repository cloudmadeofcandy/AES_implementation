from flask import Flask, render_template, request
from AES import *
app = Flask(__name__, static_folder="static")
@app.route('/')
def hello_world():
   return render_template('webinterface.html')

@app.route('/encrypt', methods = ['POST'])
def Aencrypt():
   info = ("state", "key", "IV", "cipher", "hexain", "hexakey", "hexaout", "hexaIV", "b64", "mode")
   d = {i : request.form.get(i, "False") for i in info}  
   e = encrypt(**d) 
   return {"cypherkey": e}

@app.route('/decrypt', methods = ['POST'])
def Adecrypt():
   info = ("state", "key", "IV", "cipher", "hexain", "hexakey", "hexaout", "hexaIV", "b64", "mode")
   d = {i : request.form.get(i, "False") for i in info}  
   e = decrypt(**d)
   return {"cypherkey": e}