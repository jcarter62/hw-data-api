from flask import Flask, jsonify
from waitress import serve
from appsettings import Settings
from data import ABBSites, ABBSiteData


app = Flask(__name__)

@app.route('/')
def rootPath():
    return ''

@app.route('/api/v1/sitelist', methods=['POST'])
def v1_site_list():
    data = ABBSites().sites
    jdata = jsonify(data)
    return jdata, 200

@app.route('/api/v1/site/<site_id>/<freq>/<days>', methods=['POST'])
def v1_site(site_id, freq, days):
    sd = ABBSiteData( sitename=site_id, days=days, type=freq)
    jdata = jsonify(sd.data)
    return jdata, 200

if __name__ == '__main__':
    s = Settings()
    serve(app, host=s.ip, port=s.port)

