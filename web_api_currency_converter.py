#!/usr/bin/python
import flask
from flask import request, jsonify
import currency_converter as curconv
from currency_converter import number_parser, currency_checker

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# returns the main page with a short description
@app.route('/', methods=['GET'])
def home():
    return "<h1>Kiwi Currency Converter</h1><p>This site is a prototype API for currency convertion</p>"

@app.route('/currency_converter', methods=['GET'])
def currency_converter():
    # Sample link: http://127.0.0.1:5000/currency_converter?amount=100&input_currency=EUR&output_currency=CZK
    if 'amount' in request.args:
        amount = float(request.args['amount'])
    else:
        return "<p>Error - no amount field provided. Please specify an amount to be converted into another currency.</p>"
    
    if 'input_currency' in request.args:
        input_currency = str(request.args['input_currency'])
    else:
        return "<p>Error - no input_currency field provided. Please specify an input currency.</p>"
    
    if 'output_currency' in request.args:
        output_currency = str(request.args['output_currency'])
    else:
        output_currency = None

    user_input = {
        "amount": number_parser(amount),
        "input_currency": currency_checker(input_currency),
        "output_currency": currency_checker(output_currency),
    }

    return jsonify(curconv.conversion(user_input))

if __name__ == "__main__":
    app.run()