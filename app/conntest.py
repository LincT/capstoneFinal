import urllib.request
import urllib.parse
import urllib
import requests
import json
import webbrowser
import os

req = urllib.request.urlopen("8.8.8.8", 1)
# req = urllib.request.urlopen('http://www.google.com', timeout=1)
try:
    print("{}".format(req))

except urllib.request.URLError as e:
    print(e.reason)

# hostname = "8.8.8.8"  # example
# parm = "-n" if "Windows" in os.environ["OS"] else "-c"  # -c in windows is routing compartment (admin command)
# count = 1
#
# ping_command = "ping {} {} {}".format(parm, count, hostname)
# response = os.system(ping_command)
# print("Connection to host is good" if response == 0 else "Check Connection")
