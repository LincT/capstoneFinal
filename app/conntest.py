import urllib.request
import urllib.parse
import urllib
import requests
import json
import webbrowser
import os


class ConnectionTester:
    @staticmethod
    def conn_check(host_ipv4):
        req = urllib.request.urlopen(url=host_ipv4, timeout=100)
        # req = urllib.request.urlopen('http://www.google.com')
        try:
            return "{}".format(req)

        except urllib.request.URLError as e:
            return e.reason

    @staticmethod
    def conn_check2(host_ipv4):
        hostname = host_ipv4  # example
        parm = "-n" if "Windows" in os.environ["OS"] else "-c"  # -c in windows is routing compartment (admin command)
        count = 1

        ping_command = "ping {} {} {}".format(parm, count, hostname)
        response = os.system(ping_command)
        return "Connection to host is good" if response == 0 else "Check Connection"
