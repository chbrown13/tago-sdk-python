import requests # Used to make HTTP requests
import json # Used to parse JSON
import os # Used to infer environment variables

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'

class Analysis:
    def __init__(self, token):
        self.token = token
        self.default_headers = { 'content-type': 'application/json', 'Device-Token': token }

        return

    def list(self):
        return requests.get('{api_endpoint}/analysis'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

    def create(self, data):
    	data = data if data else {}
    	return requests.post('{api_endpoint}/analysis'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(data)).json()

    def edit(self, analyze_id, data):
    	data = data if data else {}
    	return requests.put('{api_endpoint}/analysis/{analyze_id}'.format(api_endpoint=API_TAGO, analyze_id=analyze_id), headers=self.default_headers, data=json.dumps(data)).json()

    def delete(self, analyze_id):
    	return requests.delete('{api_endpoint}/analysis/{analyze_id}'.format(api_endpoint=API_TAGO, analyze_id=analyze_id), headers=self.default_headers).json()

    def info(self, analyze_id):
    	# if analyze_id is null, then call list
    	if analyze_id is None or analyze_id == '':
	    return self.list()

    	return requests.get('{api_endpoint}/analysis/{analyze_id}'.format(api_endpoint=API_TAGO, analyze_id=analyze_id), headers=self.default_headers).json()

    def run(self, analyze_id, scope):
    	return requests.post('{api_endpoint}/analysis/{analyze_id}/run'.format(api_endpoint=API_TAGO, analyze_id=analyze_id), headers=self.default_headers, data=scope).json()

    def listening(self, analyze_id, func, realtime):
    	#do something not sure yet
    	return None

    def stopListening(self, analyze_id, realtime):
    	#also do something, not sure yet
    	return None

    def tokenGenerate(self, analyze_id):
    	return requests.get('{api_endpoint}/analysis/{analyze_id}/token'.format(api_endpoint=API_TAGO, analyze_id=analyze_id), headers=self.default_headers).json()

    def uploadFile(self, file_name, file):
    	#think this is how we have to do it, using the variable names as the 'keys'
    	data = {}
    	data['file'] = file
    	data['file_name'] = file_name

    	return requests.post('{api_endpoint}/analysis/{analyze_id}/upload'.format(api_endpoint=API_TAGO, analyze_id=analyze_id), headers=self.default_headers, data=json.dumps(data)).json()





