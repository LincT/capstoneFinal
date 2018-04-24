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
        # self.UserCache.drop_table(self.table_name)
        self.UserCache.create_table(self.table_name,
                                    'user_id integer PRIMARY KEY AUTOINCREMENT, '
                                    'username text NOT NULL UNIQUE, '
                                    'password_hash text NOT NULL,'
                                    'utc_datetime_added text NOT NULL,'
                                    'locked ')

    def __str__(self):
        """
        might refactor this to live in sql_handler
        :return:
        """
        tables = [str(each) for each in self.UserCache.spew_tables()]
        verbose_table_data = ""
        for each in tables:
            fields = ", ".join(item for item in self.UserCache.spew_header(each))
            contents = "\n".join("\t\t" + str(item) for item in self.UserCache.execute_query(each))
            verbose_table_data += str("table: " + each + "\n\tfields: " + fields + "\n\tcontents:\n" + contents)

        return verbose_table_data

    def add_user(self, username, password):
        pass

    def remove_user(self, username):
        pass

    def validate_user(self):
        pass
