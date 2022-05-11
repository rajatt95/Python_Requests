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
import requests

# Base URL: http://216.10.245.166
# Library/Addbook.php


# POST request
response = requests.post('http://216.10.245.166/Library/Addbook.php',
                         # Request Body
                         json={"name": "1_Learn Test Automation", "isbn": "bcd1212121", "aisle": "227",
                               "author": "UDEMY - Rahul Shetty"},
                         # 3rd argument takes information like Header
                         headers={'Content-Type': 'application/json'},
                         # 4th argument - Optional
                         )

# No need to convert response into text and then, into Dictionary
responseInJSON = response.json()
print(responseInJSON)
print(type(responseInJSON))  # <class 'dict'>

print(response.status_code)
print(response.headers)

# {'Msg': 'successfully added', 'ID': 'bcd1212121227'}
print(responseInJSON['msg'])
# print(responseInJSON['ID'])
