#This script checks for a few different HTTP headers relevant to cyber security. Headers checked for are taken from OWASP. 


import requests as req
import json
from http.server import BaseHTTPRequestHandler
from io import BytesIO
from colorama import Fore, Back, Style, init

class HTTPRequest(BaseHTTPRequestHandler):
    def __init__(self, request_text):
        self.rfile = BytesIO(request_text)
        self.raw_requestline = self.rfile.readline()
        self.error_code = self.error_message = None
        self.parse_request()

    def send_error(self, code, message):
        self.error_code = code
        self.error_message = message

i = 1
while i < 2:
    print("Please enter a URL in this format: google.com")

    userURL = input("Please provide the URL you would like to scan: ")

    url = "https://" + userURL 

    response = req.get(url)

    headers = response.headers
    headerKeys = response.headers.keys()

#Check headers
    if 'Strict-Transport-Security' in headerKeys:
        print("Strict-Transport-Security: " + Fore.RED + "PRESENT")
        print(Style.RESET_ALL)
    else:
        print("Strict-Transport-Security: " + Fore.GREEN + "ABSENT")
        print(Style.RESET_ALL)

    if 'X-Content-Type-Options' in headerKeys:
        print("X-Content-Type-Options: " + Fore.RED + "PRESENT")
        print(Style.RESET_ALL)
    else:
        print("X-Content-Type-Options: " + Fore.GREEN + "ABSENT")
        print(Style.RESET_ALL)

    if 'Content-Security-Policy' in headerKeys:
        print("Content-Security-Policy: " + Fore.RED + "PRESENT")
        print(Style.RESET_ALL)
    else:
        print("Content-Security-Policy: " + Fore.GREEN + "ABSENT")
        print(Style.RESET_ALL)
    
    if 'X-Powered-By' in headerKeys:
        print("X-Powered-By: " + Fore.RED + "ABSENT")
        print(Style.RESET_ALL)
    else:
        print("X-Powered-By: " + Fore.GREEN + "PRESENT")
        print(Style.RESET_ALL)

    if 'X-Frame-Options' in headerKeys:
        print("X-Frame-Options: " + Fore.RED + "ABSENT")
        print(Style.RESET_ALL)
    else:
        print("X-Frame-Options: " + Fore.GREEN + "PRESENT")
        print(Style.RESET_ALL)

    printHeaderKeys = print(input("Would you like to dump the header info?: Y/N\n"))
    if printHeaderKeys == "Y" or "y":
        print(headerKeys)
    else:
        continue

    
    print("Type EXIT to exit, or AGAIN to test another URL")
    if input() == "EXIT":
        i += 1
        exit()
    if input() == "AGAIN":
        i = 1
        break
    else:
        print("Please type either EXIT or AGAIN")
