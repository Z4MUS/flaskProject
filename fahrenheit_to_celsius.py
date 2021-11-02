from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Celsius/Fahrenheit calculator: add /c/(degrees fahrenheit) to convert from fahrenheit to celsius and /f/(degrees celsius) to convert from celsius to fahrenheit</h1>'


@app.route('/c')
@app.route('/c/<fahrenheit>')
def c(fahrenheit=0):
    celsius = (fahrenheit - 32) * 5/9
    return f"{fahrenheit} in celsius is: {celsius}"


@app.route('/f')
@app.route('/f/<celsius>')
def f(celsius=0):
    fahrenheit = (celsius * 9/5) + 32
    return f"{celsius} in fahrenheit is: {fahrenheit}"


if __name__ == '__main__':
    app.run()
