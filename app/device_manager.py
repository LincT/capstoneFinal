# code to hold server info
# should keep track of server dns if applicable
# also server name, and list of emails to contact for alerts
# does not actually send alerts though


from app.sql_handler import DataBaseIO as dbio  # sql handler, really some of my handiest code


class DeviceManager:

    DeviceCache = dbio('device_database')
    table_name = 'devices'

    def __init__(self):
        """
        create a class instance to manage users and access
        """
        # self.DeviceCache.drop_table(self.table_name)
        self.DeviceCache.create_table(self.table_name,
                                      'device_id integer PRIMARY KEY AUTOINCREMENT, '
                                      'utc_datetime_added text NOT NULL,'
                                      'device_name text NOT NULL UNIQUE, '
                                      'dns text, '
                                      'ipv4 text, '
                                      'port integer, '
                                      'check_interval integer, '
                                      'recheck_interval integer, '
                                      'notifications_list text NOT NULL, '
                                      'recurring_downtime text, '
                                      'maintenance_downtime text'
                                      )

    def __str__(self):
        fields = ", ".join(item for item in self.DBCache.spew_header(self.table_name))
        contents = "\n".join("\t\t" + str(item) for item in self.DeviceCache.execute_query(self.table_name))
        table_data = str("table: " + self.table_name + "\n\tfields: " + fields + "\n\tcontents:\n" + contents)
        return table_data

    def add_device(self):
        # this needs a whole lot of input validation
        # TODO validate all the things!!!
        utc_datetime_added = self.DeviceCache.get_date_time()
        device_name = input("please enter the device name to add:\n")
        dns = input("dns for service(if applicable, enter for none)\n")
        ipv4 = input("ipv4 address\n")
        port = int(input("port number?\n"))
        check_interval = int(input("how often should it be checked in minutes?\n"))
        recheck_interval = int(input("if it fails, how soon should the system recheck in minutes?\n"))
        notifications_list = [].append(input("who should the system email first for issues?\n"))
        field_names = "utc_datetime_added, device_name, dns, ipv4, port, " \
                      "check_interval, recheck_interval, notifications_list"
        print("\n".join(
            [utc_datetime_added, device_name, dns, ipv4, port, check_interval, recheck_interval, notifications_list]))
        if input("confirm add?")[0].lower() == "y":
            self.DeviceCache.add_record(self.table_name, field_names,
                                        utc_datetime_added, device_name, dns, ipv4, port,
                                        check_interval, recheck_interval, notifications_list)

    def remove_device(self):
        device_name = input("what device do you wish to remove?\n")
        pass

    def modify_device(self):
        pass

    def spew_devices(self):
        self.DeviceCache.execute_query(self.table_name)
