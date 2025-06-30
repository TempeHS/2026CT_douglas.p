from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/aboutthesite.html')
@app.route('/')
def aboutthesite():
    card_data = (
        ("The Talt","A amazing intelligent race", "visit", "static/images/the talt.png", "/talt.html"),
        ("Star-Ships", "The wonderous star ships", "Take a look", "static/images/Spaceships.png", "/starships.html"),
        ("Humanity","we were born on this rock, we wont die here ", "see how far we have come", "static/images/we were born here.png", "/humanity.html"),
    )
    return render_template("aboutthesite.html", cards=card_data), 200

@app.route('/contact.html')
def contact():
    return render_template("contact.html"), 200

@app.route('/earth.html')
def earth():
    headings = [
        ("intro", "Title"),
        ("Heading-two", "Heading two"),
    ]
    return render_template("earth.html", active_page="earth", headings=headings), 200

@app.route('/fartworld.html')
def fartworld():
    return render_template("fartworld.html", active_page="fartworld"), 200

@app.route('/redworld.html')
def redworld():
    return render_template("redworld.html", active_page="redworld"), 200

@app.route('/skult.html')
def skult():
    headings = [
        ("intro", "Title"),
        ("Heading-two", "skult location"),
    ]
    return render_template("skult.html", active_page="skult", headings=headings), 200

@app.route('/generalinfo.html')
def generalinfo():
    return render_template("generalinfo.html", active_page="generalinfo"), 200

@app.route('/talt.html')
def talt():
    headings = [
        ("intro", "Title"),
        ("Heading-two", "Talt biology"),
        ("Heading-three", "Early Talt technology"),
    ]
    return render_template("talt.html", active_page="talt", headings=headings), 200

@app.route('/starships.html')
def starships():
    return render_template("starships.html", active_page="starships",), 200

@app.route('/humanity.html')
def humanity():
    headings = [
        ("intro", "Title"),
        ("Heading-two", "early space age"),
        ("Heading-three", "first contact"),
        ("Heading-four", "where are we now?"),
    ]
    return render_template("humanity.html", active_page="humanity",headings=headings), 200


if __name__ == '__main__':
    app.run(debug=True)
