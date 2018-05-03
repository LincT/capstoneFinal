# business logic should live here.
import logging  # https://docs.python.org/3/howto/logging-cookbook.html
import datetime


def show_menu(options_list):
    """
    :type options_list: list
    """
    # displays a list of choices and then returns user result
    options_list.append("quit")
    menu = "Please choose from one of the available options: \n"
    for option in options_list:
        menu += "{}:\t{}\n".format(list(options_list).index(option)+1, option)
    choice = input(menu)
    return choice


def timed_execution(increment=1):
    # get current_second
    current_second = int(datetime.datetime.utcnow().strftime("%S"))

    if (current_second == 0) or (current_second % increment == 0):
        # do the thing
        return True


def main():
    options = [
        "user_administration",
        "add monitoring",
        "manual server check",
    ]
    print(show_menu(options))


if __name__ == '__main__':
    main()
