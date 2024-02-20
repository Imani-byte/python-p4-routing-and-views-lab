#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return f'<p>Printed in console: {param}</p>'

@app.route('/count/<int:param>')
def count(param):
    numbers = '<br>'.join(str(i) for i in range(1, param+1))
    return f'<p>{numbers}</p>'

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = eval(f'{num1} {operation} {num2}')
    return f'<p>Result: {result}</p>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)