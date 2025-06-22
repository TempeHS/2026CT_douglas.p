from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/aboutthesite.html')
@app.route('/')
def aboutthesite():
    card_data = (
        ("The Talt","Come meet one of the first alien races humanity encountered", "visit", "static/images/the talt.png", "/talt.html"),
        ("Star-Ships", "The wonderous star ships", "Take a look", "static/images/Spaceships.png"),
        ("Humainity","we were born on this rock, we wont die here ", "see how far we have come", "static/images/we were born here.png"),
    )
    return render_template("aboutthesite.html", cards=card_data), 200

@app.route('/contact.html')
def contact():
    return render_template("contact.html"), 200
@app.route('/earth.html')
def earth():
    return render_template("earth.html"), 200

@app.route('/fartworld.html')
def fartworld():
    return render_template("fartworld.html"), 200

@app.route('/redworld.html')
def redworld():
    return render_template("redworld.html"), 200

@app.route('/skult.html')
def skult():
    return render_template("skult.html"), 200

@app.route('/generalinfo.html')
def generalinfo():
    return render_template("generalinfo.html"), 200

@app.route('/talt.html')
def talt():
    return render_template("talt.html"), 200


if __name__ == '__main__':
    app.run(debug=True)
