from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/.')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<room>')
def room(room):
    return render_template('index.html')

@app.route("/api/chat/<room>", methods=["GET", "POST"])
def room_chat(room):

    room_file_path = f"rooms/{room}.txt"

    if request.method == "POST":
        return "yuval implement"
    else:
        try:
            with open(room_file_path, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            return ""  # Return empty string if file does not exist


if __name__== "__main__":
    app.run()

