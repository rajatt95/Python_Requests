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


from PythonRequests.Z_Utilities.Configurations import getConfig
from PythonRequests.Z_Utilities.Resources import API_Resources

config = getConfig()

application_BaseURL = config['API']['application_Base_URL']
api_resource = API_Resources.getBook

print(application_BaseURL) # http://216.10.245.166/
print(api_resource) # Library/GetBook.php

print(application_BaseURL+api_resource) # http://216.10.245.166/Library/GetBook.php





