from flask import Flask, render_template, request 
from datetime import datetime
import os 
from models import db
from models.room import Room  # Import models to ensure they are registered
from models.message import Message

app = Flask(__name__)
app.config.from_object("config")

# Initialize the database
db.init_app(app)

# Implemented by Itay
@app.route('/.')
@app.route('/')
def home():
    return render_template('index.html')

# Implemented by Yuval
@app.route('/<room>')
def room(room):
        return render_template('index.html')
    
# Implemented by Itay

@app.route("/api/chat/<room>", methods=["GET", "POST"])
def api(room):

    room_file_path = f"rooms/{room}.txt"

    if request.method == "POST":
        usr = request.form["username"]
        msg = request.form["msg"]
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Ensure the room exists or create it
        room_entry = Room.query.filter_by(room_name=room).first()
        if not room_entry:
            room_entry = Room(room_name=room)
            db.session.add(room_entry)
            db.session.commit()

        # Insert the message into the database
        new_message = Message(room_name=room, user=usr, message=msg, date=date)
        db.session.add(new_message)
        db.session.commit()


    else:
        messages = Message.query.filter_by(room_name=room).order_by(Message.date.asc()).all()
        return "\n".join([
            f"[{msg.date.strftime('%Y-%m-%d %H:%M:%S')}] {msg.user}: {msg.message}"
            for msg in messages
        ])



if __name__== "__main__":
    app.run(host='0.0.0.0')

