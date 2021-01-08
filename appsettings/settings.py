import os


class Settings:

    def __init__(self):
        self.message = []
        self.ip = self.get_env('APP_IP', '0.0.0.0')
        self.port = self.get_env('APP_PORT', 5000)
        self.sql_svr = self.get_env('APP_SQL_SVR', '')
        self.sql_trusted = self.get_env('APP_SQL_TRUSTED', 'n')
        self.sql_username = self.get_env('APP_SQL_USER', '')
        self.sql_password = self.get_env('APP_SQL_PASSWORD', '')
        self.sql_db = self.get_env('APP_SQL_DB', '')

        if self.message.__len__() > 0:
            print('Warning:')
            for i in range(self.message.__len__()):
                print(self.message[i])

    def get_env(self, varname, default):
        try:
            value = os.environ.get(varname)
        except:
            value = None
        if value is None:
            value = default
            self.message.append('{} not defined'.format(varname))
        return value

