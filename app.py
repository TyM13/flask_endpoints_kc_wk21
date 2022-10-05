import json
import dbhelper
from flask import Flask, request


app = Flask(__name__)


@app.get('/api/client_info')
def get_client_info():
    client_info = dbhelper.run_statment('CALL client_info()')
    if(type(client_info) == list):
        client_info_json = json.dumps(client_info, default=str)
        return client_info_json
    else:
        return 'sorry their was a problem'


@app.get('/api/loyal_clients')
def loyal_clients_info():
    min_points = request.args.get('min_points')
    loyal_clients = dbhelper.run_statment('CALL loyalty_filter(?)', [min_points])
    if(type(loyal_clients) == list):
        loyal_clients_json = json.dumps(loyal_clients, default=str)
        return loyal_clients_json
    else:
        return 'sorry their was a problem'

app.run(debug=True)