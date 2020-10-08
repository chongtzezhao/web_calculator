from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/plus', methods=["GET", "POST"])
def addition():
    if request.method == "GET":
        return render_template('plus.html')
    elif request.method == "POST":
        a = request.form.get('plus1', 0)
        b = request.form.get('plus2', 0)
        c = int(a) + int(b)
        return render_template('plused.html', a=a, b=b, c=c)

    
@app.route('/minus', methods=["GET", "POST"])
def minus():
    if request.method == "GET":  # returns form for subtraction
        return render_template('plus.html')
    elif request.method == "POST":
        a = request.form.get('minus1', 0)
        b = request.form.get('minus2', 0)
        c = int(a) - int(b)
        return render_template('minused.html', a=a, b=b, c=c)

    
@app.route('/times', methods=["GET", "POST"])
def times():
    if request.method == "GET":
        return render_template('times.html')
    elif request.method == "POST":
        a = request.form.get('times1', 0)
        b = request.form.get('times2', 0)
        c = a * b
        return render_template('minused.html', a=a, b=b, c=c)


if __name__ == "__main__":
    app.run()
