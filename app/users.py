# code to manage adding, editing, validating, and removing users.
# sql managed

from project.sql_handler import DataBaseIO as dbio

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
                                    'locked ')

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
