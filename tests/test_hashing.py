from unittest import TestCase, main
from app.sql_handler import DataBaseIO
from app.hash import HashHandler
from os import remove, listdir


class TestMain(TestCase):
    database = None
    cursor = None

    def setUp(self):
        # things that happen before every test
        print('SetUp')
        # setup the database, connection, and cursor,
        # if this fails verify class init method working properly and
        # all arguments passed to init correctly

        self.database = DataBaseIO(':memory:')
        self.cursor = self.database.__cur__

    def tearDown(self):
        # things that happen after every test
        print('tearDown')
        pass

    @classmethod
    def setUpClass(cls):
        # things that happen at the very start of the series of tests
        print('setUpClass')
        pass

    @classmethod
    def tearDownClass(cls):
        # things that happen at the very end of the series of tests
        print('tearDownClass')
        pass

    # the actual tests
    def test_check_hash(self):
        word_list = "November Echo Victor Echo Romeo " \
                    "Golf Oscar November November Alpha " \
                    "Romeo Uniform November " \
                    "Alpha Romeo Oscar Uniform November Delta " \
                    "Alpha November Delta " \
                    "Delta Echo Sierra Echo Romeo Tango " \
                    "Yankee Oscar Uniform".split()
        for each in word_list:
            hashed_password = HashHandler.hash_password(each)
            validation = HashHandler.check_password(hashed_password=hashed_password, user_password=each)
            self.assertTrue(validation)

    def test_check_hash_from_database(self):
        # full crud test w/ a table (should probably split this into smaller tests at some point)
        # check that we can add a table w/ some data
        print("check_hash_from_database")
        table_name = "test_table"
        password = "spider"
        password2 = password + "web"
        self.database.create_table(table_name, "password_hash TEXT")
        self.assertIn("test_table", str(self.database.spew_tables()))
        self.database.add_record(table_name, '', "'{}'".format(HashHandler.hash_password(password)))

        results = self.database.execute_query(table_name, "password_hash")[0][0]
        # check if record present
        self.assertTrue(HashHandler.check_password(user_password=password, hashed_password=results))
        self.assertFalse(HashHandler.check_password(user_password=password2, hashed_password=results))


if __name__ == '__main__':
    main()
