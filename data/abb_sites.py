import pyodbc
from .connection import Connection
import copy


class ABBSites:

    def __init__(self):
        self.sites = []
        self.site_list()

    #
    # load self.parcels with data
    #
    def site_list(self):
        result = []
        conn = pyodbc.connect(Connection().connection_string)
        cursor = conn.cursor()
        cmd = 'select distinct sitename from Total_Readings order by sitename;'
        try:
            for row in cursor.execute(cmd):
                one_row = self._extract_row(row)
                record = {'name': one_row['sitename'].rstrip()}
                result.append(record)
        except Exception as e:
            print(str(e))
        self.sites = copy.deepcopy(result)
        return

    def _extract_row(self, row):
        r = {}
        i = 0
        for item in row.cursor_description:
            name = item[0]
            val = str(row[i])
            name = name.lower()
            i += 1
            r[name] = val
        return r