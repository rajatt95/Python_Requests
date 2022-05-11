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

# https://docs.python-requests.org/en/master/user/authentication/

# Basic Authentication
# ------
# Making requests with HTTP Basic Auth is very simple:

# >>> from requests.auth import HTTPBasicAuth
# >>> requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))
# <Response [200]>

# ------
# In fact, HTTP Basic Auth is so common that Requests provides a handy shorthand for using it:
#
# >>> requests.get('https://api.github.com/user', auth=('user', 'pass'))
# <Response [200]>
