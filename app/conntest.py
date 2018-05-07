import socket
from contextlib import closing
import os
from subprocess import DEVNULL, STDOUT, check_call


class ConnectionTester:
    @staticmethod
    def conn_check(host, port):
        print("socket good" if ConnectionTester.check_socket(host, port, 1) == 0 else "socket failure")
        print("ping good" if ConnectionTester.ping_check(host) == 0 else "ping failure for host")
        print("dns good" if ConnectionTester.ping_check("www.google.com") == 0 else "dns failure")
        print("network connection good" if ConnectionTester.ping_check("8.8.8.8") == 0 else "network failure")
        print("loopback good" if ConnectionTester.ping_check("127.0.0.1") == 0 else "loopback failure")
        print("\n")

    @staticmethod
    def check_socket(host, port, timeout=1):
        # https://stackoverflow.com/a/35370008
        # https://docs.python.org/3/library/socket.html#socket.socket.settimeout
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(timeout)
            return sock.connect_ex((host, port))

    @staticmethod
    def ping_check(hostname):
        # -c in windows is routing compartment (admin command)
        parm = "-n" if "Windows" in os.environ["OS"] else "-c"
        count = 1

        ping_command = "ping {} {} {}".format(parm, count, hostname)
        # response = os.system(ping_command)
        # https://stackoverflow.com/questions/5596911/python-os-system-without-the-output
        response = check_call(ping_command, stdout=DEVNULL, stderr=STDOUT)
        # return "Connection to host is good" if response == 0 else "Check Connection"
        return response
