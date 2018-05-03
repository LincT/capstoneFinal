import urllib.request
import urllib.parse
import urllib
import socket
from contextlib import closing
import os


class ConnectionTester:
    @staticmethod
    def conn_check(host, port):
        print("socket good" if ConnectionTester.check_socket(host, port, 1) == 0 else "Check socket")
        print("ping good" if ConnectionTester.ping_check(host) == 0 else "ping failed for host")
        print("ping good" if ConnectionTester.ping_check("www.google.com") == 0 else "possible dns issue")
        print("ping good" if ConnectionTester.ping_check("8.8.8.8") == 0 else "possible connection issue")
        print("ping good" if ConnectionTester.ping_check("127.0.0.1") == 0 else "loopback ping failed")

    @staticmethod
    def check_socket(host, port, timeout):
        # https://stackoverflow.com/a/35370008
        # https://docs.python.org/3/library/socket.html#socket.socket.settimeout
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(timeout)
            return sock.connect_ex((host, port))

    @staticmethod
    def ping_check(host_ipv4):
        hostname = host_ipv4  # example
        parm = "-n" if "Windows" in os.environ["OS"] else "-c"  # -c in windows is routing compartment (admin command)
        count = 1

        ping_command = "ping {} {} {}".format(parm, count, hostname)
        response = os.system(ping_command)
        # return "Connection to host is good" if response == 0 else "Check Connection"
        return response
