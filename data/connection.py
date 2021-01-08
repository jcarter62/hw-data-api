from appsettings import Settings


class Connection:

    def __init__(self):
        self.connection_string = self._conn_str_()

    def _conn_str_(self, ):
        settings = Settings()
        server = settings.sql_svr
        database = settings.sql_db
        result = 'DRIVER={ODBC Driver 17 for SQL Server}'
        result = result + ';SERVER=' + server + ';DATABASE=' + database + ';'
        if settings.sql_trusted.lower() == 'y':
            result = result + 'Trusted_Connection=yes;'
        else:
            result = result + 'UID={};PWD={}'.format(settings.sql_username, settings.sql_password)
        return result

