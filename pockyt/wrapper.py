"""
Simplified Wrappers
"""

import os
import sys
import webbrowser
from collections import OrderedDict

import requests


class SuppressedStdout(object):

    def __init__(self):
        self.stdout_fileno = -1

    def __enter__(self):
        devnull = open(os.devnull, 'w')
        self.stdout_fileno = os.dup(sys.stdout.fileno())
        os.dup2(devnull.fileno(), 1)

    def __exit__(self, *args):
        os.dup2(self.stdout_fileno, 1)


class Network(object):

    @staticmethod
    def post_request(link, payload):
        req = requests.post(link, json=payload)

        if req.status_code != 200:
            print('Error {0}! : {1}'.format(
                req.headers.get('X-Error-Code'),
                req.headers.get('X-Error'),
            ))
            sys.exit(1)
        else:
            # preserve json response ordering, as per API
            req.api_json = req.json(object_pairs_hook=OrderedDict) or {}
            return req


class Browser(object):

    @staticmethod
    def open(link, new=0, autoraise=True):
        with SuppressedStdout():
            webbrowser.open(
                url=link,
                new=new,
                autoraise=autoraise,
            )

    @classmethod
    def open_new_window(cls, link):
        cls.open(link, new=1)

    @classmethod
    def open_new_tab(cls, link):
        cls.open(link, new=2)
