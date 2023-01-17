#!/usr/bin/python3
import json  """ The json module allows you to work with JSON data in Python. It provides functions for parsing JSON data and converting Python objects to JSON"""
import urllib.request  """ The urllib.request module provides functions for opening URLs, sending HTTP requests, and handling the response. It is used to make a GET request to the REST API"""
import sys  """ The sys module provides functions and variables used to manipulate different parts of the Python runtime environment. It is used to get command-line arguments passed to the script"""


def get_employee_name(employee_id):
    """Function to get employee name"""
    url = "https://jsonplaceholder.typicode.com/users/" + str(employee_id)  """ construct the url with employee id """
    response = urllib.request.urlopen(url)  # use the urlopen function to send a GET request to the url and assign the response to the variable
    data = json.loads(response.read())  # use the json.loads function to convert the response from json format to a Python object
    return data['name']  # return the employee name from the data


def get_employee_tasks(employee_id):
    """ Function to get employee's tasks """
    url = "https://jsonplaceholder.typicode.com/todos?userId=" + str(employee_id)  # construct the url with employee id
    response = urllib.request.urlopen(url)  # use the urlopen function to send a GET request to the url and assign the response to the variable
    data = json.loads(response.read())  # use the json.loads function to convert the response from json format to a Python object
    return data  # return the employee's tasks

if len(sys.argv) < 2:  """ check if an employee id was passed as an argument """
    print("Error: Please provide an employee ID as an argument.")
    sys.exit(1)

employee_id = int(sys.argv[1])  # get the employee id passed as an argument and convert it to int

employee_name = get_employee_name(employee_id)  # call the get_employ
