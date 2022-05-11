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

# response = requests.get("https://api.github.com/user/repos", auth=('your-github-account-email',
# 'your-github-account-password'))
#
# response = requests.get("https://api.github.com/user/stars", auth=('your-github-account-email',
# 'your-github-account-password'))
#
# response = requests.get("https://api.github.com/user/repos-public", auth=('your-github-account-email',
# 'your-github-account-password'))

# -------------------------------------------------------------

# Authentication
session = requests.session()
session.auth = auth = ('your-github-account-email', 'your-github-account-password')

# Now, call all APIs

# session -> has the knowledge about Authentication
response = session.get("https://api.github.com/user/repos")

response = session.get("https://api.github.com/user/stars")

response = session.get("https://api.github.com/user/repos-public")
