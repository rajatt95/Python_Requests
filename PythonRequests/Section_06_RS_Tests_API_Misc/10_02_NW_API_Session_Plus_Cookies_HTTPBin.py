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

# https://httpbin.org/#/Cookies/get_cookies

# Authentication
# session = requests.session()
# session.auth = auth = ('your-github-account-email', 'your-github-account-password')

# Cookies
session = requests.session()
session.cookies.update = ({'common-cookie-for-all-requests': 'Dummy Common Cookie for all Requests'})

cookie_dummyCookie = {'specific-cookie-for-a-request': 'Specific Cookie for a Request'}

# Send Cookie - 'dummy-cookie' with URL
# response = requests.get('https://httpbin.org/cookies', cookies=cookie_dummyCookie)
response = session.get('https://httpbin.org/cookies', cookies=cookie_dummyCookie)

print(response.status_code)  # 200

# Expecting the cookie sent in Response Body
print(response.text)  # {
# "cookies": {
#     "common-cookie-for-all-requests": "Dummy Common Cookie for all Requests"
#     "specific-cookie-for-a-request": "Specific Cookie for a Request"
#   }
# }
