from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route("/training/<prof>")
def training(prof):
    print("инженер" in prof or "строитель" in prof)
    return render_template("base.html", t=prof)


app.run(port=8080, host='127.0.0.1')
