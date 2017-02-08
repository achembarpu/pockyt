from __future__ import absolute_import, print_function, unicode_literals, with_statement

import json
import os
import sys
import traceback
import webbrowser
from collections import OrderedDict
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

from .api import API


def print_bug_report(message=''):
    """
    Prints a usable bug report
    """

    separator = '\n' + ('-' * 69) + '\n'

    python_version = str(sys.version_info[:3])
    arguments = '\n'.join(arg for arg in sys.argv[1:])

    try:
        import pip
    except ImportError:
        packages = '`pip` is not installed !'
    else:
        packages = '\n'.join(
            '{0} - {1}'.format(package.key, package.version)
            for package in pip.get_installed_distributions()
        )

    print(
        '```{0}Bug Report :\n'
        '`pockyt` has encountered an error ! '
        'Please submit this bug report at \n` {1} `.{0}'
        'Python Version : {2}{0}'
        'Installed Packages :\n{3}{0}'
        'Runtime Arguments :\n{4}{0}'
        'Error Message :\n{5}{0}```'.format(
            separator, API.ISSUE_URL, python_version,
            packages, arguments, message or traceback.format_exc().strip()
        )
    )


class SuppressedStdout(object):
    """
    Suppresses STDOUT, utilize with the `with` keyword
    """

    def __init__(self):
        self.orig_stdout = sys.stdout.fileno()
        self.copy_stdout = os.dup(self.orig_stdout)
        self.devnull = None

    def __enter__(self):
        self.devnull = open(os.devnull, 'w')
        os.dup2(self.devnull.fileno(), self.orig_stdout)

    def __exit__(self, *args):
        os.dup2(self.copy_stdout, self.orig_stdout)
        self.devnull.close()


class Response(object):
    """
    Wraps a urllib request to provide a common python 2/3 API
    """

    def __init__(self, response):
        self._response = response

        self.code = self._get_code()
        self.info = response.info()
        self.encoding = self.get_param('charset') or API.ENCODING
        self.text = response.read().decode(self.encoding)
        self.data = self._get_data()

    def _get_code(self):
        try:  # python 3
            code = self._response._get_code()
        except AttributeError:  # python 2
            code = self._response.getcode()
        return code

    def _get_data(self):
        try:
            data = json.loads(
                self.text,
                object_pairs_hook=OrderedDict,
            )
        except ValueError:
            data = {}
        return data

    def get_header(self, key):
        try:  # python 3
            value = self._response.getheader(key)
        except AttributeError:  # python 2
            value = self.info.getheader(key)
        return value

    def get_param(self, key):
        try:  # python 3
            value = self.info.get_param(key)
        except AttributeError:  # python 2
            value = self.info.getparam(key)
        return value

    def get_qs(self):
        return urlparse.parse_qs(self.text)


class Network(object):
    """
    Safe POST Request, with error-handling
    """

    @staticmethod
    def post_request(link, payload):
        request_data = json.dumps(payload).encode(API.ENCODING)
        headers = {
            'Content-Type': API.CONTENT_TYPE,
            'Content-Length': len(request_data)
        }
        request = Request(link, request_data, headers)
        response = Response(urlopen(request))

        if response.code != 200:
            print_bug_report('API Error {0} ! : {1}'.format(
                response.get_header('X-Error-Code'),
                response.get_header('X-Error'),
            ))
            sys.exit(1)
        else:
            return response


class Browser(object):
    """
    Silently open browser windows/tabs
    """

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
