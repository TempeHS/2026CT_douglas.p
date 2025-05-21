from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("The Talt","One of the first alien races humanity encountered", "come visit", "static/images/the talt.png"),
        ("Star-Ships", "The wonderous star ships", "Take a look", "static/images/logo.png"),
        ("Humainity","we were born on this rock, we wont die here ", "see how far we have come", "static/images/logo.png"),
        
    )
    return render_template("index.html"), 200

if __name__ == '__main__':
    app.run(debug=True)
