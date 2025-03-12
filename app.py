from flask import Flask, render_template, request
from datetime import datetime
import os 


app = Flask(__name__)

@app.route('/.')
@app.route('/')
def home():
    return render_template('index.html')

# Implemented by Yuval
@app.route('/<room>')
def room(room):
        return render_template('index.html')
    

@app.route("/api/chat/<room>", methods=["GET", "POST"])
def api(room):

    room_file_path = f"rooms/{room}.txt"

# Implemented by Yuval
    if request.method == "POST":
        usr = request.form["username"]
        msg = request.form["msg"]
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")



        os.makedirs("rooms", exist_ok=True)

        if not os.path.isfile(room_file_path):
            with open(room_file_path, 'w', encoding='utf-8') as file:
                file.write(f"[{date}] {usr} : {msg}\n") 
        else:
            with open(room_file_path, 'a', encoding='utf-8') as file:
                file.write(f"[{date}] {usr} : {msg}\n") 

        return f"Message saved: [{date}] {usr} : {msg}"
    else:
        try:
            with open(room_file_path, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            return ""  # Return empty string if file does not exist



if __name__== "__main__":
    app.run()

