# /**
# * @author Rajat Verma
# * https://www.linkedin.com/in/rajat-v-3b0685128/
# * https://github.com/rajatt95
# * https://rajatt95.github.io/
# *
# * Course: Learn API Automation Testing with Python & BDD Framework (https://www.udemy.com/course/python-sdet-rest-api-automation/)
# * Tutor: Rahul Shetty (https://www.udemy.com/user/rahul445/)
# */
#
# /***************************************************/

# https://realpython.com/python-requests/
# https://docs.python-requests.org/en/latest/
# Requests is an elegant and simple HTTP library for Python, built for human beings.
import json

import requests

# Base URL: http://216.10.245.166
# /Library/GetBook.php?AuthorName=somename

# GET request
response = requests.get('http://216.10.245.166/Library/GetBook.php',
             # Query param
             params={'AuthorName': 'Rahul Shetty2'},
             # 3rd argument takes information like Header
             # We are leaving it blank because this API does not require any headers
             )

print(response.headers) # {'Date': 'Mon, 09 May 2022 20:12:13 GMT', 'Server': 'Apache', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'POST', 'Access-Control-Max-Age': '3600', 'Access-Control-Allow-Headers': 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With', 'Keep-Alive': 'timeout=5, max=100', 'Connection': 'Keep-Alive', 'Transfer-Encoding': 'chunked', 'Content-Type': 'application/json;charset=UTF-8'}

print(response.headers['Access-Control-Allow-Methods']) # POST
print(response.headers['Server']) # Apache

# Assertions
assert response.headers['Access-Control-Allow-Methods'] == 'POST'
assert response.headers['Server'] == 'Apache'
