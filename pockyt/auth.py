"""
Pocket API Access Authenticator
"""

import configparser
import os
import sys
import urllib.parse

from .api import API
from .wrapper import Network


class Authenticator(object):

    def __init__(self, args):
        self._args = args
        self._config = None
        self._consumer_key = None
        self._request_token = None
        self._access_token = None
        self._username = None

        self._config_path = os.path.join(
            os.path.expanduser('~'),
            '.{0}'.format(API.APP_NAME),
        )

    @property
    def credentials(self):
        return {
            'consumer_key': self._consumer_key,
            'access_token': self._access_token,
            'username': self._username,
        }

    def _save_config(self):
        self._config = configparser.ConfigParser()

        self._config['CREDENTIALS'] = self.credentials

        with open(self._config_path, 'w+') as cf:
            self._config.write(cf)

    def _load_config(self):
        self._config = configparser.ConfigParser()
        self._config.read(self._config_path)

    def _obtain_request_token(self):
        payload = {
            'consumer_key': self._consumer_key,
            'redirect_uri': API.REDIRECT_URL,
        }
        req = Network.post_request(API.REQUEST_TOKEN_URL, payload)
        info = urllib.parse.parse_qs(req.text)

        self._request_token = info['code'][0]

    def _obtain_access_token(self):
        payload = {
            'consumer_key': self._consumer_key,
            'code': self._request_token,
        }
        req = Network.post_request(API.ACCESS_TOKEN_URL, payload)
        info = urllib.parse.parse_qs(req.text)

        self._access_token = info['access_token'][0]
        self._username = info['username'][0]

    def _setup(self):
        input('Create an application, via this link :\n` {0} `\n'
              'Press Enter when done...'
              .format(API.APP_CREATE_URL))

        self._consumer_key = input('Enter your Consumer Key: ')

        self._obtain_request_token()

        input('Connect an account, via this link :\n` {0} `\n'
              'Press Enter to when done...'
              .format(API.AUTHORIZE_USER_URL(self._request_token)))

        self._obtain_access_token()

        self._save_config()

        print('Welcome {0} !\n{1} is now ready for usage !'
              .format(self._username, API.APP_NAME))

    def _load(self):
        self._load_config()
        try:
            credentials = self._config['CREDENTIALS']
        except KeyError:
            print('Connect an account first!')
            sys.exit(1)
        else:
            self._consumer_key = credentials['consumer_key']
            self._access_token = credentials['access_token']
            self._username = credentials['username']

    def run(self):
        if self._args.do == 'register':
            self._setup()
            sys.exit(0)
        else:
            self._load()
            return
