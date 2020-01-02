import os
from twilio.rest import Client

class WhatsApp:
    def __init__(self, sid = None, auth = None, from_number = None, to_number = None):
        self.sid            = sid
        self.auth           = auth
        self.from_number    = from_number
        self.to_number      = to_number
        self.client         = client
        self._authenticate()
        self._configure_client()

    def _configure_client(self):
        self.client = Client(self.sid, self.auth)

    def _authenticate(self):
        if (self.sid is None or self.auth is None):
            self.sid, self.auth = os.environ.get('TWILIO_ACCOUNT_SID'), os.environ.get('TWILIO_AUTH_TOKEN')
        if (self.sid is None or self.auth is None):
            raise Exception('cannot authenticate Twillio credentials. Invalid credentials.')

    def send(self, message):
        self.client.messages.create(body = message, from_= self.from_number, to=self.to_number)