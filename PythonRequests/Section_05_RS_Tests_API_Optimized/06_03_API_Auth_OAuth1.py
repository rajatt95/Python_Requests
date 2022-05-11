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

# OAuth 1
# ------

# Authentication A common form of authentication for several web APIs is OAuth. The requests-oauthlib library
# allows Requests users to easily make OAuth 1 authenticated requests:
#
# >>> import requests
# >>> from requests_oauthlib import OAuth1
#
# >>> url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
# >>> auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
# ...               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
#
# >>> requests.get(url, auth=auth)
# <Response [200]>
