

def show_menu(options_list):
    # displays a list of choices and then returns user result
    menu = ""
    for option in options_list:
        menu = "{}: {}\n".format(option, list(options_list).index(option))
    print(menu)
    choice = input("Please choose from the available options")
    if choice in range(len(options_list)):
        return choice


def main():
    options = [
        "user_administration",
        "add monitoring",
        "manual server check",
        "stop program"
    ]
    print(show_menu(options))


if __name__ == '__main__':
    main()
