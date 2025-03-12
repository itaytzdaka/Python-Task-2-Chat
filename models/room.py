from models import db  # Import the shared db instance

class Room(db.Model):

    __tablename__ = 'rooms'  # Ensure the correct table name is used

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    room_name = db.Column(db.String(255), unique=True, nullable=False)

    # Relationship: One room can have many messages
    messages = db.relationship("Message", backref="room", cascade="all, delete", lazy=True)

    def __repr__(self):
        return f"<Room {self.room_name}>"