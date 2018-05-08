import logging  # https://docs.python.org/3/howto/logging-cookbook.html
import datetime
import time
from collections import namedtuple

from app.users import UserManager
from app.device_manager import DeviceManager
import app.email_manager as alerts
import threading
from app.conntest import ConnectionTester
from app import config

devices = DeviceManager()
users = UserManager()

logging.basicConfig(filename="event_log.log", level=logging.INFO)
logger = logging.getLogger('network_events')


def show_menu(options_list):
    """
    :type options_list: list
    """
    valid_selection = False
    while not valid_selection:
        # displays a list of choices and then returns user result

        menu = "Please choose from one of the available options: \n"
        for option in options_list:
            menu += "{}:\t{}\n".format(options_list.index(option) + 1, option)
        choice = input(menu)
        if choice.isnumeric():
            if int(choice) <= len(options_list):
                return options_list[int(choice)-1]

        elif choice in options_list:
            return choice
        else:
            continue


def timed_execution(increment=1):
    # get current_minute and add 1 to avoid division by 0 error
    current_minute = int(datetime.datetime.utcnow().strftime("%M"))+1

    # to determine if we are to do the thing, see if the chosen increment
    # divides perfectly into the current second (1-60)
    if current_minute % increment == 0:
        # do the thing
        return True
    else:
        return False


def user_administration():
    # placeholder for integrating user management class to ui
    print("user_administration ran")
    pass


def monitoring():
    options = {
        "list all": devices.spew_devices,
        "add device": devices.add_device,
        "update device": devices.modify_device,
        "remove device": devices.remove_device,
    }
    selection = show_menu([each for each in options.keys()])
    options[selection]()  # call the function from the dictionary

    pass


def manual_server_check():
    host = input("host dns or ipv4?\n")
    port = input("port on host to check?\n")
    if host == "demo":
        ConnectionTester.conn_check("map.minectc.com", 80)
    else:
        if port.isnumeric():
            port = int(port)
            success = "socket check successful for port {} on {}".format(port, host)
            failure = "no response from port {} on {}".format(port, host)
            print(success if ConnectionTester.check_socket(host=host, port=port) == 0 else failure)
        else:
            success = "ping successful for {}".format(host)
            failure = "ping failed to reach {}".format(host)
            print(success if ConnectionTester.ping_check(hostname=host) == 0 else failure)


def run_service():
    device = namedtuple("device", ["device_id", "utc_datetime_added", "device_name", "dns", "ipv4", "port",
                                   "check_interval", "recheck_interval", "notifications_list",
                                   "recurring_downtime", "maintenance_downtime"])

    current_alerts = {}
    main_failure = False
    while True:
        debug_url = "www.google.com"  # TODO these should be user configurable
        debug_ipv4 = "8.8.8.8"
        if ConnectionTester.ping_check(debug_url) != 0:  # verify dns services can resolve a known ip
            logging.warning("{} dns resolution for {} failed".format(datetime.datetime, debug_url))
            if ConnectionTester.ping_check(debug_ipv4) != 0:  # if not check if known good ip resolves
                # both ip4 and dns down, checking devices becomes irrelevant, hold status until those resolve
                # if that fails individual devices behind the server cannot function
                logging.error("ping {} failed".format(debug_ipv4))
                continue  # continue service to check for recovery

        else:
            if main_failure:
                message_string = "Network failure was detected. This alert indicates possible recovery"
                send_email(subject="network recovery", email=config.RECIPIENT, message=message_string)

            device_list = devices.spew_devices()  # check for updated list
            if device_list:
                for each in device_list:
                    map(device, each)
                    if device.dns != "":  # if a dns is specified for the device
                        if ConnectionTester.check_socket(str(device.dns), str(device.port)) != 0:
                            logging.warning("port failure for {}".format(device.device_name))
        time.sleep(60)


def send_email(**kwargs):
    """
    message     specifies the main body of the email to be sent

    subject     specifies what is put into the title of the email

    recipient   must be a valid email, otherwise the email will
                not reach it's target
    """

    if kwargs:  # if there's arguments, then we can process
        message = kwargs.get("message", "")
        recipient = kwargs.get("email", None)
        subject = kwargs.get("subject", "")
        alerts.send_email(recipient=recipient, message_string=message, subject=subject)
    else:  # get user to input values if no kwargs
        recipient = input("destination email:\n")
        subject = input("subject:\n")
        message = input("message to send:\n")
        if input("send message?\n")[0].lower() == "y":
            alerts.send_email(recipient=recipient, message_string=message, subject=subject)


def quit_program():
    # wrapper function
    exit(0)


def user_interface():
    auth = False
    while not auth:
        auth = users.validate_user()

    options = {
        "user administration": user_administration,
        "manage monitoring": monitoring,
        "manual server check": manual_server_check,
        "send test email": send_email,
        # "run service": run_service,
        "quit": quit_program  # wrapper for exit, only exists to simplify menu code
    }
    selection = show_menu([each for each in options.keys()])
    options[selection]()  # call the function from the dictionary
    user_interface()


def main():
    main_task = threading.Thread(target=user_interface)  # need to drop () when specifying target
    daemon = threading.Thread(target=run_service, daemon=False)

    main_task.start()
    daemon.start()

    main_task.join()
    daemon.join()


if __name__ == '__main__':
    main()
