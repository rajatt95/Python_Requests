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

# https://www.rahulshettyacademy.com/

# Cookie -> 'visit-month'

# Cookie has to be sent as Dictionary

cookie_visitMonth = {'visit-month': 'April'}

# Send Cookie with URL
# response = requests.get('https://www.rahulshettyacademy.com/', cookies=cookie_visitMonth)
response = requests.get('https://www.rahulshettyacademy.com/', cookies=cookie_visitMonth,
                        allow_redirects=False)

print(response.history)  # [<Response [301]>]
print(response.status_code)  # 200
