import logging  # https://docs.python.org/3/howto/logging-cookbook.html
import datetime
import time
from collections import namedtuple

from app.users import UserManager
from app.device_manager import DeviceManager
import app.email_manager as alerts
import threading
from app.conntest import ConnectionTester

devices = DeviceManager()
users = UserManager()

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
    print("user_administration ran")


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
    port = int(input("port on host to check?\n"))
    ConnectionTester.conn_check(host=host, port=port)


def run_service():
    device = namedtuple("device",
                        "device_id "
                        "utc_datetime_added "
                        "device_name "
                        "dns "
                        "ipv4 "
                        "port "
                        "check_interval, "
                        "recheck_interval, "
                        "notifications_list "
                        "recurring_downtime "
                        "maintenance_downtime")
    device_data = devices.spew_devices()

    if device_data is None:
        print("no devices setup for monitoring")

    else:
        while True:
            for each in devices.spew_devices():
                map(device, each)
            # print("service running", time.gmtime())
            time.sleep(60)


def send_alert():
    pass


def send_email():
    print("send email function")
    pass


def quit_program():
    exit(0)


def user_IO():
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
    user_IO()

def main():

    daemon = threading.Thread(target=run_service(), daemon=True)
    main_task = threading.Thread(target=user_IO())

    main_task.start()
    daemon.start()

    main_task.join()


if __name__ == '__main__':
    main()
