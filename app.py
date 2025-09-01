from flask import render_template, flash, redirect, session, url_for, request, g, Flask
import json
from processors import async_group
import pythonnet
import clr
import requests as RQS

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/add_me', methods=['POST'])
def add_me():
    """
    Method that adds two numbers
    :return: str
    """
    data_string = request.get_data()
    data = json.loads(data_string)

    first_number = data['first_number']
    second_number = data['second_number']
    answer = first_number + second_number

    return f"{answer}"

@app.route('/multiply_me', methods=['POST'])
def multiply_me():
    """
    Method that multiplies two numbers
    :return: str
    """
    data_string = request.get_data()
    data = json.loads(data_string)

    first_number = data['first_number']
    second_number = data['second_number']
    answer = first_number * second_number

    return f"{answer}"

@app.route('/cube_me', methods=['POST'])
def cube_me():
    """
    Method that cubs a number
    :return: str
    """
    data_string = request.get_data()
    data = json.loads(data_string)

    first_number = data['first_number']
    answer = first_number ** 3

    return f"{answer}"


# if __name__ == '__main__':
#     app.run(debug=True)
