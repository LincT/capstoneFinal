# code to hold server info
# should keep track of server dns if applicable
# also server name, and list of emails to contact for alerts
# does not actually send alerts though
# peewee

from app.sql_handler import DataBaseIO as dbio  # sql handler, really some of my handiest code


class DeviceCache:

    DeviceCache = dbio('device_database')
    table_name = 'devices'

    def __init__(self):
        """
        create a class instance to manage users and access
        """
        # self.DBCache.drop_table(self.table_name)
        self.DeviceCache.create_table(self.table_name,
                                      'device_id integer PRIMARY KEY AUTOINCREMENT, '
                                      'device_name text NOT NULL UNIQUE, '
                                      'notifications_list text NOT NULL,'
                                      'utc_datetime_added text NOT NULL,'
                                      'recurring_downtime text,'
                                      'maintenance_downtime text')

    def __str__(self):
        fields = ", ".join(item for item in self.DBCache.spew_header(self.table_name))
        contents = "\n".join("\t\t" + str(item) for item in self.DeviceCache.execute_query(self.table_name))
        table_data = str("table: " + self.table_name + "\n\tfields: " + fields + "\n\tcontents:\n" + contents)
        return table_data

    def add_device(self):
        device_name = input("please enter the device name to add:\n")

        pass

    def remove_device(self, username):
        pass

    def modify_device(self,):
        pass
