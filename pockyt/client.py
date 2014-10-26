from __future__ import absolute_import, print_function, unicode_literals

try:
    input = raw_input
except NameError:
    pass

import sys
import time

import parse

from .api import API
from .wrapper import Browser, Network


class Client(object):
    """
    Pocket API Access Client
    """

    def __init__(self, credentials, args):
        self._args = args
        self._credentials = credentials
        self._api_endpoint = ''
        self._payload = {}
        self._req = None

        self._format_spec = ''
        self._unformat_spec = None
        self._output = []
        self._input = []

    def _api_request(self):
        # add API access credentials
        self._payload.update(self._credentials)

        # access API
        self._req = Network.post_request(self._api_endpoint, self._payload)

    def _print_to_file(self):
        with open(self._args.output, 'w+') as outfile:
            for info in self._output:
                line = self._format_spec.format(**info)
                try:
                    outfile.write(line)
                except UnicodeEncodeError:
                    outfile.write(line.encode('utf-8'))

    def _print_to_console(self):
        for info in self._output:
            line = self._format_spec.format(**info)
            try:
                print(line, end='')
            except UnicodeEncodeError:
                print(line.encode('utf-8'), end='')

    def _open_in_browser(self):
        # open a new window
        Browser.open_new_window(self._output[0]['link'])

        for info in self._output[1:]:
            # open new tabs
            Browser.open_new_tab(info['link'])
            # pace webbrowser actions
            time.sleep(2)

    def _get_console_input(self):
        print('Enter data: {0}'.format(self._args.format.strip()))
        try:
            while True:
                data = input().strip()
                if data:
                    info = self._unformat_spec.parse(data)
                    self._input.append(info)
                else:
                    raise EOFError
        except EOFError:
            pass

    def _get_redirect_input(self):
        for line in sys.stdin.readlines():
            data = line.strip()
            if data:
                info = self._unformat_spec.parse(data)
                self._input.append(info)
            else:
                continue

    def _get_file_input(self):
        with open(self._args.input, 'r') as f:
            for line in f.readlines():
                data = line.strip()
                if data:
                    info = self._unformat_spec.parse(data)
                    self._input.append(info)
                else:
                    continue

    def _validate_format(self):
        # interpret escape sequences
        try:
            self._args.format = bytes(
                self._args.format, 'utf-8'
            ).decode('unicode_escape')
        except TypeError:
            self._args.format = self._args.format.decode('unicode_escape')

        keys = ['id', 'title', 'link', 'excerpt', 'tags']
        info = dict((key, None) for key in keys)

        try:
            self._args.format.format(**info)
        except KeyError:
            print('Invalid Format Specifier!')
            sys.exit(1)
        else:
            self._format_spec = self._args.format + '\n'
            self._unformat_spec = parse.compile(self._args.format)

    def _get(self):
        # create request payload
        payload = {
            'state': self._args.state,
            'sort': self._args.sort,
        }

        if self._args.content != 'all':
            payload['contentType'] = self._args.content

        if self._args.count != -1:
            payload['count'] = self._args.count

        if self._args.query:
            payload['search'] = self._args.query

        if self._args.tag == '-1':
            pass
        elif self._args.tag == '0':
            payload['tag'] = '_untagged_'
        else:
            payload['tag'] = self._args.tag

        if self._args.favorite != -1:
            payload['favorite'] = self._args.favorite

        if self._args.domain:
            payload['domain'] = self._args.domain

        self._payload = payload
        self._api_endpoint = API.RETRIEVE_URL

        self._api_request()

        json_data = self._req.api_json
        items = json_data.get('list') or {}

        if len(items) == 0:
            print('No items found!')
            sys.exit(0)

        self._output = [
            {
                'id': item.get('item_id'),
                'title': item.get('resolved_title'),
                'link': item.get('resolved_url'),
                'excerpt': item.get('excerpt'),
                'tags': item.get('tags'),
            }
            for item in items.values()
        ]

    def _put(self):
        payload = {'actions': []}

        for info in self._input:
            payload['actions'].append({
                'action': 'add',
                'url': info['link'],
            })

        self._payload = payload
        self._api_endpoint = API.MODIFY_URL

        self._api_request()

    def _modify(self):
        payload = {'actions': []}

        action = ''
        if self._args.delete:
            action = 'delete'
        elif self._args.archive != -1:
            if self._args.archive == 1:
                action = 'archive'
            else:
                action = 'readd'
        elif self._args.favorite != -1:
            if self._args.favorite == 1:
                action = 'favorite'
            else:
                action = 'unfavorite'

        for info in self._input:
            payload['actions'].append({
                'action': action,
                'item_id': info['id'],
            })

        self._payload = payload
        self._api_endpoint = API.MODIFY_URL

        self._api_request()

    def run(self):

        # validate format specifier
        self._validate_format()

        if self._args.do == 'get':
            self._get()

            # print output
            self._print_to_console()

            # redirect output
            if self._args.output == 'browser':
                self._open_in_browser()
            elif self._args.output:
                self._print_to_file()

        else:
            if self._args.input == 'console':
                self._get_console_input()
            elif self._args.input == 'redirect':
                self._get_redirect_input()
            else:
                self._get_file_input()

            if self._args.do == 'put':
                self._put()
            elif self._args.do == 'mod':
                self._modify()
