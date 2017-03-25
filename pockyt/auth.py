from __future__ import absolute_import, print_function, unicode_literals, with_statement

try:
    input = raw_input
except NameError:
    pass

try:
    import ConfigParser as configparser
except ImportError:
    import configparser

import os
import sys

from .api import API
from .wrapper import Browser, Network


class Authenticator(object):
    """
    Pocket API Access Authenticator
    """

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
        self._config.add_section(API.CONFIG_HEADER)
        for (k, v) in self.credentials.items():
            self._config.set(API.CONFIG_HEADER,  k, v)

        with open(self._config_path, 'w+') as f:
            self._config.write(f)

    def _load_config(self):
        self._config = configparser.ConfigParser()
        self._config.read(self._config_path)

    def _obtain_request_token(self):
        payload = {
            'consumer_key': self._consumer_key,
            'redirect_uri': API.REDIRECT_URL,
        }
        response = Network.post_request(API.REQUEST_TOKEN_URL, payload)
        qs = response.get_qs()

        self._request_token = qs['code'][0]

    def _obtain_access_token(self):
        payload = {
            'consumer_key': self._consumer_key,
            'code': self._request_token,
        }
        response = Network.post_request(API.ACCESS_TOKEN_URL, payload)
        qs = response.get_qs()

        self._access_token = qs['access_token'][0]
        self._username = qs['username'][0]

    def _setup(self):
        print('Note: During the registration process, pockyt will attempt to '
              'open the required links in your default browser. '
              'If any errors occur, you can use the printed links instead.\n')

        create_link = API.APP_CREATE_URL

        Browser.open_new_tab(create_link)

        input('Step 1:\nCreate an application, via this link :\n` {0} `\n'
              'Press Enter when done...'.format(create_link))

        self._consumer_key = input('Step 2:\nEnter your Consumer Key: ')

        self._obtain_request_token()

        auth_link = API.get_auth_user_url(self._request_token)

        Browser.open_new_tab(auth_link)

        input('Step 3:\nConnect an account, via this link :\n` {0} `\n'
              'Press Enter when done...'.format(auth_link))

        self._obtain_access_token()

        self._save_config()

        print('Welcome {0} !\n{1} is now ready for usage !'
              .format(self._username, API.APP_NAME))

    def _load(self):
        self._load_config()
        try:
            self._consumer_key = self._config.get(API.CONFIG_HEADER, 'consumer_key')
            self._access_token = self._config.get(API.CONFIG_HEADER, 'access_token')
            self._username = self._config.get(API.CONFIG_HEADER, 'username')
        except (configparser.NoSectionError, KeyError):
            print('Please connect an account first, by running `pockyt reg` !')
            sys.exit(1)

    def run(self):
        if self._args.do == 'reg':
            self._setup()
            sys.exit(0)
        else:
            self._load()
            return
