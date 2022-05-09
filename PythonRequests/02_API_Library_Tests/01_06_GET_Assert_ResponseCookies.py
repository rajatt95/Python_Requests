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

# print(response.cookies)
# print(response.headers['Access-Control-Allow-Methods']) # POST
# print(response.headers['Server']) # Apache
#
# # Assertions
# assert response.headers['Access-Control-Allow-Methods'] == 'POST'
# assert response.headers['Server'] == 'Apache'
