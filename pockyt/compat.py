try:  # py2
    prompt = raw_input
except NameError:
    prompt = input

try:  # py2
    import ConfigParser as configparser
except ImportError:
    import configparser

try:  # py2
    import urlparse
except ImportError:
    import urllib.parse as urlparse

try:
    from urllib.request import urlopen, Request
except ImportError:  # py2
    from urllib2 import urlopen, Request
