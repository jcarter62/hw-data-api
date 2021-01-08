import pyodbc
from .connection import Connection
import copy


class ABBSiteData:

    def __init__(self, sitename='', days=30, type='4PerDay'):
        self.sitename = sitename
        self.days = days
        self.type = type
        self.csv = 'No'
        self.data = []
        self._getdata_()

    #
    # load self.parcels with data
    #
    def _getdata_(self):
        result = []
        conn = pyodbc.connect(Connection().connection_string)
        cursor = conn.cursor()
        cmd_str = "exec sp_30DaySiteReadings @SiteName='{}', @Days={}, @Type='{}', @CSV='{}';"
        cmd = cmd_str.format(self.sitename, self.days, self.type, self.csv)
        try:
            for row in cursor.execute(cmd):
                one_row = self._extract_row(row)
                # 'row' = {str}'1'
                # 'sitename' = {str}'10L       '
                # 'chname' = {str}'A BRL     '
                # 'readingdate' = {str}'2020.12.09'
                # 'readingtime' = {str}'12:00'
                # 'reading' = {str}'14518.27'
                # 'consumption' = {str}'0.0000'
                # 'averagecfs' = {str}'0.0000'

                record = {
                    'name': one_row['sitename'].rstrip(),
                    'channel': one_row['chname'].rstrip(),
                    'date': one_row['readingdate'].rstrip(),
                    'time': one_row['readingtime'].rstrip(),
                    'reading': float(one_row['reading']),
                    'consumption': float(one_row['consumption']),
                    'avg_cfs': float(one_row['averagecfs'])
                }
                result.append(record)
        except Exception as e:
            print(str(e))
        self.data = copy.deepcopy(result)
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