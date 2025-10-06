Terms in this set (39)

Your stats
Not studied (39)
You haven't studied these terms yet.

Select these 39
What is the primary defense against log injection attacks?
Sanitize outbound log messages


import logging
import sys
import logging
import sys
#log division by zero error to the log, the output is printed to the screen
def divideByZeroError(dividend, divisor):
logging.basicConfig(stream=sys.stdout,format='%(levelname)s:%(message)s')

try:
quotient = dividend/divisor
print (quotient)

except Exception as e:
#logging error here, use str(e) as part of the output
if __name__ == '__main__':
dividend = int(input())
divisor = int(input())

divideByZeroError(dividend,divisor)
logging.error("The exception that occured is: %s", str(e))


An attacker exploits a cross-site scripting vulnerability.
Access the user's data


Which Python function is prone to a potential code injection attack?
eval()


What are two common defensive coding techniques?
Check functional and preconditions and postconditions


# unit test case
import unittest
def multiply_numbers(x, y):
#add your code here
return x * y
# add your code here


class TestForNone(unittest.TestCase):

def test_when_a_is_null(self):
try:
self.assertIsNone(multiply_numbers(5, None))
except AssertionError as msg:
print(msg)
if __name__ == '__main__':
unittest.main()
if x is None:
print("x is a null value")
return y
elif y is None:
print("y is a null value")
return x
else:
return x * y


Which package is meant for internal use by Python for regression testing?
test


from string import Template
CONFIG = {
"API_KEY": "'you've just exposed your secret_key'"
}
class User:
name = ""
email = ""
def __init__(self, name, email):
self.name = name
self.email = email
def __str__(self):
return self.name

if __name__ == '__main__':
name = input()
email = input()

user = User(name, email)

# FIXME: Here is where you want to use the template class
print(f"The secret is {user.__init__.__globals__['CONFIG']['API_KEY']}")
t = Template("Hello, my name is $n.")
print(t.substitute(n=user.name))


import time

class Limiter:
def __init__(self, rate, per):
self.rate = rate
self.per = per
self.bucket = rate
self.last_check = time.time()
def limit(self, callback_fn):
current = time.time()
time_passed = current - self.last_check
self.last_check = current

# Finish line 18 by writing an expression that determines the value of the bucket
# Use the following variables in your expression: time_passed, self.bucket, self.rate, and self.per
bucket = # Insert your expression here

if (bucket > self.rate):
self.bucket = self.rate
if (bucket < 1):
pass
else:
callback_fn()
self.bucket = bucket - 1
bucket = self.bucket + (time_passed * self.rate / self.per)


def CelciusToFahrenheit(Temperature):
#insert assert statement for, "Colder than zero degrees Celsius!"
return ((Temperature*9)/5)+32
if __name__ == '__main__':
Temperature = int(input())
try:
print(CelciusToFahrenheit(Temperature))
except AssertionError as msg:
print(msg)
assert Temperature >= 0, "Colder than zero degrees Celsius!"


# verify we only have digits
def check_numeric_value(wg_int):
return isinstance(wg_int, int)

#return true if numeric value is an integer, else return false.
#Hint: use isinstance function
# verify if the string is null
def check_null_string (wg_string):


# check if wg_string is not null return true else return false

if __name__ == '__main__':

wg_string = "I like dogs." # use keyword None to test
wg_int = 12345

print(check_null_string (wg_string))
print(check_numeric_value(wg_int))
return isinstance(wg_int, int)

return wg_string is not None


def hash_password(pwd):
# encode password string to bytes
enc_pwd = pwd.encode()

# call the sha256(...) function returns a hash object
d = hashlib.sha256(enc_pwd)

# generate binary hash of password string in hexidecimal
hash = d.digest()

return hash

if __name__ == '__main__':
pwd = input()

print(hash_password(pwd))
d = hashlib.sha3_256(enc_pwd)

hash = d.hexdigest()


from generate_key import generate_key
from deserialize import deserialize
from serialize import serialize
def safe_deserialize(key, serialized_data):
new_key = '' # replace the empty string with a newly generated key

try:
if key == new_key:
return # return deserialized data when validation passes
else:
raise Exception('New key does not match old key')
except Exception as error:
print('Error:', error)

return False
# Example usage
grades = {'Alice': 89, 'Bob': 72, 'Charles': 87}
serialized_data = serialize(grades)
deserialized_data = safe_deserialize(generate_key(serialized_data), serialized_data)
new_key = generate_key(serialized_data)

return deserialize(serialized_data)


isValidNumber = False
while not isValidNumber:
try:
pickedNumber = int(input('Pick a number from 1 to 10'))
if pickedNumber >= 1 and pickedNumber <= 10:
isValidNumber = True
except:
print('You must enter a valid number from 1 to 10')
print('You picked the number ' + str(pickedNumber))
Type and range check


import requests
urls = open("websites.txt", "r")

for url in urls:
url = url.strip()
req = requests.get(url)
print (url, 'report😂

try:transport_security = req.headers['Strict-Transport-Security']except:print ('HSTS header not set properly')
Man-in-the-middle


#check if the zipcode input is numeric
if __name__ == '__main__':

zipCode = input()
try:
#check that zip code is an integer value
print(f'Your zip code is {zipCode}.')
except:
print('Please use numeric digits for the zip code.')
zipCode = int(zipCode)


#check if the length of the password is at least 8 characters
if __name__ == '__main__':

password = input()

#write an if / else statement to evaluate passwords length
if(len(password) >= 8):
print("Your password is long enough.")
else:
print("Your password is too short.")


#check if the input range is between 1 and 10 for the range validation check
if __name__ == '__main__':

r = range(1,10)

num = int(input())

# create conditional statement for range check here
r = range(1,11)

num = int(input())

if num in r:
print("The number input is in the range from 1 and 10.")
else:
print("The number input is not in the range from 1 and 10.")


A security analyst has noticed a vulnerability in which an attacker took over multiple users' accounts.

Which vulnerability did the security analyst encounter?
Broken access control


When creating a new user, an administrator must submit the following fields to an API endpoint:

Name

Email Address

Password

IsAdmin

What is the best way to ensure the API is protected against privilege escalation?

Implement resource and field-level access control


Which method is used for a SQL injection attack?
Exploiting query parameters


import hashlib
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import os
class AESCipher(object):
def __init__(self, key):
self.block_size = AES.block_size
self.key = hashlib.sha256(key.encode()).digest()
def encrypt(self, plain_text):
plain_text = self.__pad(plain_text)
counter = self.block_size.to_bytes(self.block_size, "big")
cipher = AES.new(self.key, AES.MODE_CTR, counter=lambda: counter)
#FIX ME: encrypted_text = ?
return b64encode(counter + encrypted_text).decode("utf-8")
def __pad(self, plain_text):
number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
ascii_string = chr(number_of_bytes_to_pad)
padding_str = number_of_bytes_to_pad * ascii_string
padded_plain_text = plain_text + padding_str
return padded_plain_text
if __name__ == '__main__':
msg = input("Enter message: ")
cipher = AESCipher(msg)
#Test the message size
msg = msg*10

print(cipher.encrypt(msg))
encrypted_text = cipher.encrypt(plain_text)


import os
import stat
def admin(filename, admin):
return admin

def user(filename, user):
return user

def grant_permission(name_list, filename):
# FIXME
os.chmod(filename, stat.S_IRWXU)
check_permission(filename)
def check_permission(filename):
# Check if file path exists
path1 = os.access(filename, os.F_OK)
print("The path exists:", path1)
# Check if User has Read Access
path2 = os.access(filename, os.R_OK)
print("Access to read the file:", path2)
# Check if User has Write Access
path3 = os.access(filename, os.W_OK)
print("Access to write the file:", path3)
# Check if User has Execute Permission
path4 = os.access(filename, os.X_OK)
print("Check if path can be executed:", path4)
if os.access(filename, os.R_OK):
# open txt file as file
with open(filename) as file:
file.read()
else:
# in case can't access the file
print("Cannot access the file")
with open("output_file.txt", 'w') as f:
if os.access(filename, os.W_OK):
f.write("I have write privilege.\n")

if __name__ == '__main__':
filename = input()
name = input()
k = []
res
if result:
os.chmod(filename, stat.S_IRWXU)
else:
os.chmod(filename, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)


def authorizeAdmin(usr):
assert isinstance(usr, list) and usr != [], "No user found"
assert 'admin' in usr, "No admin found."
print("You are granted full access to the application.")

If __name__ == '__main__':
authorizeAdmin(['user'])
AssertionError: No admin found


#Simulated auhorization code
ownerID = 4567
def ShowData():
print("This is the user data")
def Redirect():
print("Redirecting to homepage")
def GetUserID():
return 1234
if(not GetUserID() == ownerID): # this is just a simulation, this line is typically !$_GET['userID'] === object.ownerID
print( "You are not allowed to view this data")
Redirect()
ShowData()
if(not GetUserID() == ownerID): # this is just a simulation, this line is typically !$_GET['userID'] === object.ownerID
print( "You are not allowed to view this data")
Redirect()
else:
ShowData()


What does cross-origin resource sharing (CORS) allow users to do?
Override same starting policy for specific resources


Which protocol caches a token after it has been acquired?
MSAL


import requests

url = 'https://website.com/'

# Get request

result = requests.get(url)

# Print request

print(result.content.decode())

403


import requests
url = 'https://api.github.com/invalid'

try:
request_response = requests.get(url)

# If the response was successful, no Exception will be raised
request_response.raise_for_status()
except Exception as err:
print(f'Other error occurred: {err}')
else:
print('Success!')
404 - Not Found


Which response method, when sent a request, returns information about the server's response and is delivered back to the console?
response.content


Status Codes
- 200 = OK
- 201 = CREATED
- 400 = BAD REQUEST
- 401 = UNAUTHORIZED
- 403 = FORBIDDEN
- 404 = NOT FOUND
- 405 = METHOD NOT ALLOWED
- 500 = INTERNAL SERVER ERROR


200
Ok


201
Created


400
Bad Request


401
Unauthorized


403
Forbidden


404
Not Found


405
Method Not Allowed


500
Internal Server Error


You can also click on terms or definitions to blur or reveal them

Review with an activity

