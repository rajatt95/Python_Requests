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
# /Library/GetBook.php?AuthorName=somename

# GET request
response = requests.get('http://216.10.245.166/Library/GetBook.php',
             # Query param
             params={'AuthorName': 'Rahul Shetty2'},
             # 3rd argument takes information like Header
             # We are leaving it blank because this API does not require any headers
             )

# No need to convert response into text and then, into Dictionary
responseInJSON = response.json()
print(type(responseInJSON)) # <class 'list'>

actualBook = ""

for book in responseInJSON:
    if book['isbn'] == '0':
        actualBook = book
        print(book['book_name'] +" | "+ book['isbn'] +" | "+book['aisle'])
        break

expectedBook = {
        "book_name": "Python",
        "isbn": "0",
        "aisle": "75"
    }

assert actualBook == expectedBook


