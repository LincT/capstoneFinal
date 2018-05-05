# code to manage adding, editing, validating, and removing users.
# sql managed
# if no users, should allow first user creation
# if last user deleted and someone tries to log in, work as new user, delete configured data and start as new app

from app.sql_handler import DataBaseIO as dbio


class UserManager:

    UserCache = dbio('user_database')
    table_name = 'users'

    def __init__(self):
        """
        create a class instance to manage users and access
        """
        # self.DBCache.drop_table(self.table_name)
        self.UserCache.create_table(self.table_name,
                                    'user_id integer PRIMARY KEY AUTOINCREMENT, '
                                    'username text NOT NULL UNIQUE, '
                                    'password_hash text NOT NULL,'
                                    'utc_datetime_added text NOT NULL,'
                                    'locked text NOT NULL')

    def __str__(self):
        fields = ", ".join(item for item in self.DBCache.spew_header(self.table_name))
        contents = "\n".join("\t\t" + str(item) for item in self.DeviceCache.execute_query(self.table_name))
        table_data = str("table: " + self.table_name + "\n\tfields: " + fields + "\n\tcontents:\n" + contents)
        return table_data

    def add_user(self, username, password):
        pass

    def remove_user(self, username):
        pass

    def validate_user(self):
        username = input("username?\n")
        password = input("password?\n")
        # TODO insert some hash validation here as we don't store passwords in our db... ever
        if username and password:
            return True
        else:
            return False
