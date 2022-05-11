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

# https://petstore.swagger.io/#/pet/uploadFile

url = 'https://petstore.swagger.io/v2/pet/9843217/uploadImage'

# This is a Dictionary
files = {'file': open('../Z_Utilities/pet.jpeg', 'rb')}

response = requests.post(url, files=files)
print(response.text)  # {"code":200,"type":"unknown","message":"additionalMetadata: null\nFile uploaded to ./pet.jpeg, 7184 bytes"}
print(response.status_code)  # 200











