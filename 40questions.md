Terms in this set (40)

Original
200 OK
Your request was successful!


201 Created
The request was accepted, and the resource was created.


400 Bad Request
Your request is either wrong or missing some information.


401 Unauthorized
Your request requires some additional permissions.


404 Not Found
The requested resource doesn't exist.


405 Method Not Allowed
The endpoint doesn't allow for that specific HTTP method


500 Internal Server Error
Your request wasn't expected and probably broke something on the server side.


What is the primary defense against log injection attacks?
Sanitize outbound log messages
3 multiple choice options


An attacker exploits a cross-site scripting vulnerability. What is the attacker able to do?

Access the user's data

3 multiple choice options


Which Python function is prone to a potential code injection attack?

eval()

3 multiple choice options


What are two common defensive coding techniques?

Check functional preconditions and postconditions

3 multiple choice options


Which package is meant for internal use by Python for regression testing?

test
3 multiple choice options


Consider the following assertion statement: 

def authorizeAdmin(usr): 

assert isinstance(usr, list) and usr != [], “No user found” 

assert ‘admin’ in usr, “No admin found.” 

print(“You are granted full access to the application.”) 

If __name__ == ‘__main__’: 

authorizeAdmin([‘user’]) 

What should be the response after running the code?

AssertionError: No admin found

3 multiple choice options


A security analyst has noticed a vulnerability in which an attacker took over multiple users’ accounts. Which vulnerability did the security analyst encounter?

Broken access control

3 multiple choice options


When creating a new user, an administrator must submit the following fields to an API endpoint: 

Name 

Email Address 

Password 

IsAdmin 

What is the best way to ensure the API is protected against privilege escalation?

Implement resource and field-level access control

3 multiple choice options


Which method is used for a SQL injection attack?

Exploiting query parameters

3 multiple choice options


What does cross-origin resource sharing (CORS) allow users to do?

Override same starting policy for specific resources

3 multiple choice options


Which protocol caches a token after it has been acquired?

MSAL

3 multiple choice options


Consider the following API code snippet: 

import requests url = 'https://website.com/' 

# Get request 

result = requests.get(url) 

# Print request print(result.content.decode()) 

Which status code will the server return?

403

3 multiple choice options


The user submits the following request to an API endpoint that requires a header: 

import requests 

url = 'https://api.github.com/invalid' 

try: 

request_response = requests.get(url) 

# If the response was successful, no Exception will be raised request_response.raise_for_status() except Exception as err:

print(f'Other error occurred: {err}') 

else: 

print('Success!') 

Which response code will the user most likely be presented with?

404—"Not found"

3 multiple choice options


Which response method, when sent a request, returns information about the server's response and is delivered back to the console?

response.content

3 multiple choice options


Which is best for input validation?
type(): The type() function is used to determine the type of an object. While it's not typically used for input validation directly, it can be used to check the type of user input to ensure it matches the expected data type (e.g., checking if an input is an integer or a string)


Which Python function is prone to a potential code injection attack?
eval()


Which Python function is used to prevent log injection?
validate()


What are two common defensive coding techniques?
Check functional and preconditions and postconditions


Checking functional and preconditions and postconditions is best practice for?
Defensive Coding


An attacker exploits a cross-site scripting vulnerability
Access User's data


A user masquerades as other users, what type of attack was used?
Cross Site Scripting


Which method is used for a SQL injection attack?
Exploiting query parameters


Exploiting query parameters causes what attack?
SQL injection


What is returned when using response.content?
returns the raw binary content of the HTTP response as bytes


Which response method, when sent a request, returns information about the server's response and is delivered back to the console?
response.content


What can an attacker do with a log injection attack
Injection of commands a parser can execute


What is the primary defense against log injection attacks?
Sanitize outbound log messages


Which package is meant for internal use by Python for regression testing?
test


Which software testing relies on using old test cases?
Regression testing


When should regression testing be conducted?
After some code changes


What does cross-origin resource sharing (CORS) allow users to do?
Override same starting policy for specific resources


Access Control Allow Origin- client request to (server) www.client.url , what does server send back? (wording?)
ACAO client.url


Which protocol caches a token after it has been acquired?
MSAL


