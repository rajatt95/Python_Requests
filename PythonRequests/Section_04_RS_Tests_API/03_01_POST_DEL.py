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
from PayLoad import *

# POST request
response_AddBook = requests.post('http://216.10.245.166/Library/Addbook.php',
                                 # Request Body
                                 json=addBookPayLoad("123f23221"),
                                 # 3rd argument takes information like Header
                                 headers={'Content-Type': 'application/json'},
                                 # 4th argument - Optional
                                 )

response_AddBook_InJSON = response_AddBook.json()
print(response_AddBook_InJSON['ID'])
book_ID = response_AddBook_InJSON['ID']

# DELETE request
response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php',
              # Request Body
              json={"ID": book_ID},
              # 3rd argument takes information like Header
              headers={'Content-Type': 'application/json'},
              # 4th argument - Optional
              )
print(response_deleteBook.status_code)
response_deleteBook_InJSON = response_deleteBook.json()
print(response_deleteBook_InJSON['msg'])
