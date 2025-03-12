from flask import Flask, render_template, request
from datetime import datetime
import os 


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<room>')
def room(room):
        return render_template('index.html')
    

@app.route('/api/chat/<room>', methods=["POST", "GET"])
def post(room):
    if request.method == "POST":
        usr = request.form["username"]
        msg = request.form["msg"]
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


        file_path = f"rooms/{room}.txt"

        os.makedirs("rooms", exist_ok=True)

        if not os.path.isfile(file_path):
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"[{date}] {usr} : {msg}\n") 
        else:
            with open(file_path, 'a', encoding='utf-8') as file:
                file.write(f"[{date}] {usr} : {msg}\n") 

        return f"Message saved: [{date}] {usr} : {msg}"
    else: 
        return "itay part"

if __name__== "__main__":
    app.run()

