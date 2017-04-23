
API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'

class SMS:
	def __init__(self, analysis_token):
		self.analysis_token = analysis_token
        self.default_headers = { 'content-type': 'application/json', 'Device-Token': analysis_token }

    # Send SMS to a number
    # to{string} : Number to send SMS, Example: +554498774411
    # message{string} :
    # Returns Promise
    def send(self, to, message):
    	data = {'to':to, 'message':message}
    	url = '{api_endpoint}/analysis/services/sms/send'.format(api_endpoint=API_TAGO)
        return requests.post(url, data=json.dumps(data), headers=self.default_headers).json()
