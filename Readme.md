# URL Validation for Emma

Intro:
This is an updated (compared to my previous git repo) URL checker based on Python 3.

Instructions To Run:
Copy and paste the Checker.py file into your favorite IDE running a Python 3 interpreter.

Notes:
HTTPS support is only available if the socket module was compiled with SSL support. This does mean that some https sites will
not validate as good, giving false failures (such as failing for not completing a SSL handshake). I tested it to work
on apple.com but see that it will fail when checking a bank webpage. This SSL work-around just avoids checking the SSL
certificate. If doing something other than validating an URL, this would not be a good solution.
