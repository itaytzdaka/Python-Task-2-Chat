from models import db

class Message(db.Model):
    __tablename__ = 'messages'  # Ensure correct table name

    id = db.Column(db.Integer, primary_key=True)
    room_name = db.Column(db.String(255), db.ForeignKey('rooms.room_name'), nullable=False)  # Fix foreign key
    user = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<Message {self.user}: {self.message}>"
