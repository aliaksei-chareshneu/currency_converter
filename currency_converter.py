#!/usr/bin/python
import argparse
import forex_python
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
import json
from configuration import currency_mapping

supported_currencies = sorted({v for item in currency_mapping.items() for v in item})

# checks if the passed currency is a currency symbol, returns currency otherwise
def currency_checker(currency):
    if currency in currency_mapping.values():
        return symbol_to_code(currency)
    return currency

# checks if the passed value is a positive number and a number at all
def number_parser(n):
    try:
        number = float(n)
        if number < 0:
            error_message = "{} is not a positive number. Please, provide a positive number instead".format(n)
            raise argparse.ArgumentTypeError(error_message)
        return number
    except ValueError:
        error_message = "{} is not a number. Please, provide a positive number instead".format(n)
        raise argparse.ArgumentTypeError(error_message)

# function converting the currency symbol to the 3 letter code
def symbol_to_code(currency_symbol):
    return {value: key for key, value in currency_mapping.items()}[currency_symbol]

# parses arguments provided by the user
def user_input_parser():
    parser = argparse.ArgumentParser(description='Convert currencies.') # what exactly is descibed?
    parser.version = '1.0' # do I need this?
    parser.add_argument( # type positive_value as a function?
        '--amount', type=number_parser, action='store', required=True, help='amount of given currency to be converted')
    parser.add_argument( # type check_currency
        '--input_currency', type=currency_checker, action='store', required=True, help='3 letter input currency code or currency symbol', choices=supported_currencies)
    parser.add_argument( # type check_currecny
        '--output_currency', type=currency_checker, action='store', required=False, help='3 letter output currency code or currency symbol', choices=supported_currencies)
    args = parser.parse_args()
    return vars(args)

# converts currency
def conversion(args):
    c = CurrencyRates()
    if (args['output_currency'] == None):
        app_output = {
            "input": {
                "amount": args['amount'],
                "currency": args['input_currency']
            },
            "output": {
            }
        }
        all_currency_rates = c.get_rates(args['input_currency'])
        for key in all_currency_rates:
            app_output["output"][key] = round(all_currency_rates[key]*args['amount'], 3)
        return app_output
    else:
        app_output = {
            "input": {
                "amount": args['amount'],
                "currency": args['input_currency']
            },
            "output": {
                args['output_currency']: round(c.convert(args['input_currency'], args['output_currency'], args['amount']), 3),
            }
        }
        return app_output

if __name__ == "__main__":
    user_input = user_input_parser()
    print(json.dumps(conversion(user_input), indent=4))