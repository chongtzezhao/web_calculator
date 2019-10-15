from flask importFlask, render template, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('plus', methods=["GET", "POST"])
def addition():
    if request.method == "GET":
        return render_template('plus.html')
    elif request.method == "POST":
        a = request.from.get('plus1', 0)
        b = request.from.get('plus2', 0)
        c =0
        for i in range(a):
            c++
        for i in range(b):
            c++
        return render_template('plused.html', a=a, b=b, c=c)

    
@app.route('minus', methods=["GET", "POST"])
def minus():
    if request.method == "GET":
        return render_template('plus.html')
    elif request.method == "POST":
        a = request.from.get('minus1', 0)
        b = request.from.get('minus2', 0)
        c =0
        for i in range(a):
            c++
        for i in range(b):
            c--
        return render_template('minused.html', a=a, b=b, c=c)


if __name__ = "__main__":
        flask.run(debug==TRUE)
