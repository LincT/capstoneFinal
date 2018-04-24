# code to hold server info
# should keep track of server dns if applicable
# also server name, and list of emails to contact for alerts
# does not actually send alerts though
# peewee

from app.sql_handler import DataBaseIO as dbio  # sql handler, really some of my handiest code


class DeviceCache:

    DeviceCache = dbio('device_database')
    table_name = 'users'

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
        """
        might refactor this to live in sql_handler
        :return:
        """
        tables = [str(each) for each in self.DBCache.spew_tables()]
        verbose_table_data = ""
        for each in tables:
            fields = ", ".join(item for item in self.DBCache.spew_header(each))
            contents = "\n".join("\t\t" + str(item) for item in self.DBCache.execute_query(each))
            verbose_table_data += str("table: " + each + "\n\tfields: " + fields + "\n\tcontents:\n" + contents)

        return verbose_table_data

    def add_user(self, username, password):
        pass

    def remove_user(self, username):
        pass

    def validate_user(self):
        pass
