from flask import Flask, render_template, request
from datetime import datetime, timezone
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration
DB_USER = "chatuser"
DB_PASSWORD = "chatpassword"
DB_HOST = os.getenv("DB_HOST", "mysql")  # Use container name for Docker
DB_NAME = "chatdb"

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Database Model for Messages
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.String(255), nullable=False)
    usr = db.Column(db.String(255), nullable=False)
    msg = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))  # ✅ Fix

    def __init__(self, room, date, usr, msg):
        self.room = room
        self.date = date
        self.usr = usr
        self.msg = msg

    def __repr__(self):
        return f"<Message {self.usr} in {self.room}>"  # ✅ Fix

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<room>')
def room(room):
    return render_template('index.html')

@app.route("/api/chat/<room>", methods=["GET", "POST"])
def api(room):
    if request.method == "POST":
        usr = request.form["username"]
        msg = request.form["msg"]
        date = datetime.now(timezone.utc)  # ✅ Fix

        new_message = Message(room=room, date=date, usr=usr, msg=msg)

        db.session.add(new_message)
        db.session.commit()

        return f"Message saved: [{date}] {usr} : {msg}"

    else:
        messages = Message.query.filter_by(room=room).order_by(Message.date.asc()).all()
        return "\n".join([f"[{msg.date}] {msg.usr} : {msg.msg}" for msg in messages])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
