import logging  # https://docs.python.org/3/howto/logging-cookbook.html
import datetime
import time
from collections import namedtuple

from app.users import UserManager as users
from app.device_manager import DeviceCache as devices
import app.email_manager as alerts
from app.conntest import ConnectionTester

def show_menu(options_list):
    """
    :type options_list: list
    """
    valid_selection = False
    options_list.append("quit")
    while not valid_selection:
        # displays a list of choices and then returns user result

        menu = "Please choose from one of the available options: \n"
        for option in options_list:
            menu += "{}:\t{}\n".format(options_list.index(option) + 1, option)
        choice = input(menu)
        if choice.isnumeric():
            if int(choice) == len(options_list):
                exit(0)
            elif int(choice) < len(options_list):
                return options_list[int(choice)-1]

        elif choice in options_list:
            if choice == options_list[-1]:
                exit(0)
            else:
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
    pass


def manual_server_check():
    host = input("host dns or ipv4?\n")
    port = int(input("port on host to check?\n"))
    ConnectionTester.conn_check(host=host, port=port)


def run_service():
    device = namedtuple("device",
                        "device_id "
                        "utc_datetime_added "
                        "device_name dns ipv4 "
                        "notifications_list "
                        "recurring_downtime "
                        "maintenance_downtime")
    while True:

        print("service running", time.gmtime())
        time.sleep(60)



def main():

    options = {
        "user administration": user_administration,
        "add monitoring": monitoring,
        "manual server check": manual_server_check,
        "send test email":send_email
        "run service": run_service
    }
    selection = show_menu([each for each in options.keys()])
    options[selection]()  # call the function from the dictionary


if __name__ == '__main__':
    main()
