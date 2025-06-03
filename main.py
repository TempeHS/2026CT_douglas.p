from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/aboutthesite.html')
@app.route('/')
def aboutthesite():
    card_data = (
        ("The Talt","One of the first alien races humanity encountered", "come visit", "static/images/the talt.png"),
        ("Star-Ships", "The wonderous star ships", "Take a look", "static/images/Spaceships.png"),
        ("Humainity","we were born on this rock, we wont die here ", "see how far we have come", "static/images/we were born here.png"),
    )
    return render_template("aboutthesite.html", cards=card_data), 200

@app.route('/contact.html')
def contact():
    return render_template("contact.html"), 200

@app.route('/world1.html')
def world1():
    return render_template("world1.html"), 200

@app.route('/world2.html')
def world2():
    return render_template("world2.html"), 200

@app.route('/world3.html')
def world3():
    return render_template("world3.html"), 200

@app.route('/world4.html')
def world4():
    return render_template("world4.html"), 200



if __name__ == '__main__':
    app.run(debug=True)
