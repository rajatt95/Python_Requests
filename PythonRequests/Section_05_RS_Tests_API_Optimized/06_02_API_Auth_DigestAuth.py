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

# Digest Authentication
# ------

# Another very popular form of HTTP Authentication is Digest Authentication, and Requests supports this out of the
# box as well:

# >>> from requests.auth import HTTPDigestAuth
# >>> url = 'https://httpbin.org/digest-auth/auth/user/pass'
# >>> requests.get(url, auth=HTTPDigestAuth('user', 'pass'))
# <Response [200]>
