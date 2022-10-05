from email.policy import default
import json
import dbhelper
from flask import Flask


app = Flask(__name__)


@app.get('/api/client_info')
def get_client_info():
    client_info = dbhelper.run_statment('CALL client_info')
    if(type(client_info) == list):
        client_info_json = json.dumps(client_info, default=str)
        return client_info_json
    else:
        return 'sorry their was a problem'

app.run(debug=True)