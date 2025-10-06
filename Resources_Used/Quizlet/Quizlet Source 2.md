Terms in this set (40)

Original
Cross-site Scripting
An attacker exploits a vulnerability to access user data.


SQL injection
Exploiting query parameters to execute a SQL injection attack.


response.content
Returns the raw binary content of the HTTP response as bytes.


Injection of commands a parser can execute
What an attacker can do with a log injection attack?


Regression testing
Software testing that relies on using old test cases.


After some code changes
When regression testing should be conducted?


Cross-origin Resource Sharing (CORS)
Allows users to override the same-origin policy for specific resources. It is a mechanism that allows or restricts web applications running at one origin (domain) to make requests for resources hosted on a different origin.


MSAL
A protocol that caches a token after it has been acquired.


bucket = rate
if bucket > rate


pass
if bucket < rate


Cross Site Scripting
a type of security flaw in web applications where an attacker can inject malicious scripts into web pages that are viewed by other users. These scripts are then executed by the users' web browsers, allowing the attacker to perform various actions on behalf of the victim.


encrypted_text = cipher.encrypt(plain_text.encode())
encrypted_text = ?


Denial of Service
Prevention: Rate Limiting
an attempt to overload a website or network, with the aim of degrading its performance or even making it completely inaccessible.


Code Injection
Prevention: input validation
occurs when an attacker is able to insert malicious code into a program. This code is then executed by the system, potentially leading to unauthorized actions, data breaches, or other harmful outcomes.


Man in the Middle
Prevention: HTTPS, up to date certificates, authenticate users/devices, avoid open wifi networks
an attacker intercepts and potentially alters communication between two parties without their knowledge. This can lead to unauthorized access, data theft, or data manipulation.


Cross Site Scripting
Prevention: Validate and Sanitize all user inputs
allows attackers to inject malicious scripts into web pages viewed by other users. This can lead to various security issues, such as unauthorized data access, session hijacking, and defacement of websites.


Broken Access Control
Prevention: Implement strong authentication and authorization, Role-Based Access Control
occurs when an application or system does not properly enforce authorization policies, allowing users to access resources or perform actions they should not be permitted to


Broken Function Level Authorization
Prevention: Role Based Access Control, Server Side Authorization Checks
an application does not properly enforce access controls for different functions or operations based on the user's role or permissions. This flaw allows users to perform actions or access functionalities that they should not be authorized to use, often leading to unauthorized access, data exposure, or manipulation.


API Mass Assignment
an application allows users to update multiple fields or attributes of an object via an API endpoint without proper validation or restrictions. This can lead to unauthorized modifications of sensitive data or unintended changes to the object's state.


Privilege Escalation
occurs when an attacker gains elevated access rights or permissions beyond those originally granted to them


MSAL
handles the acquisition, caching, and renewal of access tokens and refresh tokens, simplifying token management for developers.


Authentication
refers to giving a user permissions to access a particular resource. Since, everyone can't be allowed to access data from every URL, one would require authentication primarily. To achieve this authentication, typically one provides authentication data through Authorization header or a custom header defined by server.


LDAP
commonly used to handle directory services such as user authentication, authorization, and directory management. It is an industry standard and is widely used for various applications, including user authentication, email directories, and more.


ACL
a list of permissions associated with a network resource or object that specifies which users or systems are allowed or denied access to that resource. ACLs are used to enforce security policies and control access to resources based on various criteria.


GET Request
used to retrieve data from a specified resource on a web server. It is one of the most common HTTP methods and is used to request data without modifying or affecting the server's state. When a GET request is made, the requested data is usually returned in the response body.


response.history
provides a list of Response objects that represent the intermediate responses encountered while following redirects.
It is used to track and examine the series of responses that were encountered during the process of following redirects.
It returns a list of 'response' objects, ordered oldest to most recent, where each represents and intermediate response received as a result of a redirection.


response.status_code
represents the HTTP status code returned by the server in response to a request.


response.content
provides the raw content of the HTTP response as a byte string. This attribute is useful when you need to access the response data in its raw form, such as when dealing with binary data or when you want to perform custom processing on the raw response body. Particularly useful for images, files, or other binary formats.


rate limited requests
refers to a request that is constrained by a rate limit imposed by a server or API to control the frequency of requests from a client. Rate limiting is a technique used to prevent abuse, ensure fair usage, and maintain the performance and reliability of a service.


resource level access control
governs which users or entities can access specific resources within a system, application, or service. It is a type of access control that focuses on individual resources rather than broader, system-wide permissions. The aim is to ensure that only authorized users or entities can interact with or manipulate specific resources based on their roles, permissions, or attributes.


field-level access control
regulates access to specific fields or attributes within a resource, rather than the resource as a whole. This fine-grained access control allows for detailed management of permissions at the individual field level within data records, forms, or objects.


Man in the Middle Interception
criminal puts themselves between client and server, done via creating an unsecure wifi network, finding entry into an insecure network via packet sniffer, creaking fake websites, or manipulating IP protocols to get a user to change a pw or log into an app


Man in the Middle Decryption
Use of data capture tools to transmit any login info or web activity back to the criminal to be decrypted (get login credentials from a fake website, use it on real one)


403 - The user can reach the site but not access further (more permission needed). Headers and Cookies provide necessary data that is validated for requests


XSS Example/Explanation
Attacker inserts malicious script (generally through input fields or url parameters not properly sanitized) that is executed by other users who visit the site. The users are then prey to cookie theft, redirection to phishing sites, or their webpage may be manipulated.


400 - Bad Request
indicates that the server could not understand or process the request due to invalid syntax or bad formatting. This could happen due to various reasons such as malformed URL, missing required parameters, or incorrect data.


401 - Unauthorized
indicates that the request lacks valid authentication credentials. This often occurs when an API requires authentication (e.g., an API key, bearer token, or other credentials) and those credentials are either missing, invalid, or expired.


403 - Forbidden
indicates that the server understands the request but refuses to authorize it. This often occurs when the user or client has the correct credentials but lacks the necessary permissions to access the requested resource.


404 - Not Found
indicates that the server could not find the requested resource. This typically happens when the URL is incorrect or the resource does not exist on the server.


ACAO client.url
Access Control Allow Origin (ACAO) - client request to (server) www.client.url , what does server send back?