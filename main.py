# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

# connects /kangaroos path to render aboutus.html
@app.route('/Mini Lab Stuff/')
def Minilabs():
    return render_template("Mini Lab Stuff.html")

@app.route('/Test1/')
def test1():
    return render_template("test1.html")

# connects /kangaroos path to render aboutus.html
@app.route('/aboutus/')
def aboutus():
    return render_template("aboutus.html")

@app.route('/Homepages/')
def HomePages():
    return render_template("Homepages.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")

@app.route('/Michael/', methods=['GET', 'POST'])
def Michael():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Michael.html", name=name)
    # starting and empty input default
    return render_template("Michael.html", name="World")

@app.route('/byron/', methods=['GET', 'POST'])
def byron():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("byron.html", name=name)
    # starting and empty input default
    return render_template("byron.html", name="World")

@app.route('/ChaseHomepage/')
def CHomepage():
    return render_template("ChaseHomepage.html")

@app.route('/byronhomepage/')
def BHomepage():
    return render_template("byronhomepage.html")

@app.route('/binary/')
def binary():
    BITS = 8
    imgbulbOn = "/static/assets/bulb_on.jpg"
    if request.method == 'Post':
        BITS = int(request.form['BITS'])
        imgbulbOn = request.form['lighton']
    return render_template("Binary.html", imgbulbOn = imgbulbOn, BITS=BITS)

@app.route('/binary2/')
def binary2():
    return render_template("Binary2.html")


@app.route('/layout/')
def layout():
    return render_template("layout.html")

@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/Chase/', methods=['GET', 'POST'])
def ChaseGreeting():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Chase.html", name=name)
    # starting and empty input default
    return render_template("Chase.html", name="World")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)