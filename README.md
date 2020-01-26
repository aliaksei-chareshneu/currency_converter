# Currency converter (Python CLI & web API)

The application converts a given amount of one currency into another currency, using the forex data.
Both CLI and web API versions are available. Supported currencies are listed in the configuration.py file.

## Getting Started & Prerequisites

You will need Python 3 installed (http://www.python.org/getit/) and modules, listed in requirements.txt.

To run the app, download the application files or clone repository, and install the requirements:

``pip install --user --requirement requirements.txt``

## Use cases
### CLI application

Running the application:

``python currency_converter.py --amount <amount> --input_currency <input_currency> --output_currency [output_currency]``

Result is outputted as json.

*Note: output_currency is an optional argument. In case it is omitted, input_currency will be converted into all supported currencies*

#### Example 1:

``
./currency_converter.py --amount 100.0 --input_currency EUR --output_currency CZK
``

Output:

```json
{
    "input": {
        "amount": 100.0,
        "currency": "EUR"
    },
    "output": {
        "CZK": 2516.0
    }
}
```

#### Example 2:

``
./currency_converter.py --amount 0.9 --input_currency ¥ --output_currency AUD
``

Output:

```json
{
    "input": {
        "amount": 0.9,
        "currency": "CNY"
    },
    "output": {
        "AUD": 0.19
    }
}
```

#### Example 3:

``
./currency_converter.py --amount 10.92 --input_currency £
``

Output:

```json
{
    "input": {
        "amount": 10.92,
        "currency": "GBP"
    },
    "output": {
        "GBP": 10.92,
        "HKD": 111.087,
        "IDR": 194313.78,
        "ILS": 49.346,
        "DKK": 96.788,
        "INR": 1018.913,
        "CHF": 13.874,
        "MXN": 268.321,
        "CZK": 325.866,
        "SGD": 19.311,
        "THB": 436.772,
        "HRK": 96.38,
        "EUR": 12.952,
        "MYR": 58.098,
        "NOK": 128.708,
        "CNY": 99.092,
        "BGN": 25.331,
        "PHP": 726.489,
        "PLN": 55.129,
        "ZAR": 205.395,
        "CAD": 18.768,
        "ISK": 1779.569,
        "BRL": 59.687,
        "RON": 61.908,
        "NZD": 21.609,
        "TRY": 84.884,
        "JPY": 1566.642,
        "RUB": 882.91,
        "KRW": 16696.346,
        "USD": 14.292,
        "AUD": 20.887,
        "HUF": 4351.914,
        "SEK": 136.463
    }
}
```

### Web API application

Running the local server:

``python web_api_currency_converter.py``

Getting the conversion results in your web browser:

``http://127.0.0.1:5000/currency_converter?amount=[amount_to_be_converted]&input_currency=[currency_code_or_symbol]&output_currency=[currency_code_or_symbol]``

*Note: output_currency is an optional argument. In case it is omitted, input_currency will be converted into all supported currencies*

#### Example 4:

``
GET /currency_converter?amount=0.9&input_currency=¥&output_currency=AUD HTTP/1.1
``

Output:

```json
{
  "input": {
    "amount": 0.9, 
    "currency": "CNY"
  }, 
  "output": {
    "AUD": 0.19
  }
}
```

#### Example 5:

``
GET /currency_converter?amount=10.92&input_currency=£ HTTP/1.1
``

Output:

```json
{
  "input": {
    "amount": 10.92, 
    "currency": "GBP"
  }, 
  "output": {
    "AUD": 20.887, 
    "BGN": 25.331, 
    "BRL": 59.687, 
    "CAD": 18.768, 
    "CHF": 13.874, 
    "CNY": 99.092, 
    "CZK": 325.866, 
    "DKK": 96.788, 
    "EUR": 12.952, 
    "GBP": 10.92, 
    "HKD": 111.087, 
    "HRK": 96.38, 
    "HUF": 4351.914, 
    "IDR": 194313.78, 
    "ILS": 49.346, 
    "INR": 1018.913, 
    "ISK": 1779.569, 
    "JPY": 1566.642, 
    "KRW": 16696.346, 
    "MXN": 268.321, 
    "MYR": 58.098, 
    "NOK": 128.708, 
    "NZD": 21.609, 
    "PHP": 726.489, 
    "PLN": 55.129, 
    "RON": 61.908, 
    "RUB": 882.91, 
    "SEK": 136.463, 
    "SGD": 19.311, 
    "THB": 436.772, 
    "TRY": 84.884, 
    "USD": 14.292, 
    "ZAR": 205.395
  }
}
```

## Built With

* [forex-python](https://github.com/MicroPyramid/forex-python) - Used to convert currencies
* [Flask](http://flask.palletsprojects.com/en/1.1.x/) - The web framework used

## Contributing & Feedback

Please feel free to provide a feedback, create an issue, or contact me by email (chareshneu.tech@gmail.com)