from flask import Flask, request,render_template

app = Flask(__name__)


# @ signifies a decorator - way to wrap a function and modifying its behaviour .aka override an existing function.
@app.route('/')
def index():
    return 'Hello World,<a href="/predict">Predict</a>' \
           '<form method="post" action="/predict">' \
           '<input type=submit>' \
           '</form>'

@app.route('/predict',methods=['POST','GET'])
def predict():
    values= ["one","two","three"]

    return render_template("predict.html",name="Woo hoo man",values=values)


if __name__ == "__main__":
    app.run(debug=True)