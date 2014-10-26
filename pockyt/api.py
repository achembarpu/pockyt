from __future__ import unicode_literals


class API(object):
    """
    Pocket API Access Data
    """

    APP_NAME = 'pockyt'

    POCKET_URL = 'https://getpocket.com/'
    API_URL = POCKET_URL + 'v3/'

    REDIRECT_URL = 'https://www.github.com/arvindch/{0}'.format(APP_NAME)

    APP_CREATE_URL = 'http://getpocket.com/developer/apps/new'

    REQUEST_TOKEN_URL = API_URL + 'oauth/request'

    AUTHORIZE_USER_URL = lambda rt: \
        API.POCKET_URL + 'auth/authorize?request_token={0}' \
                         '&redirect_uri={1}'.format(rt, API.REDIRECT_URL)

    ACCESS_TOKEN_URL = API_URL + 'oauth/authorize'

    RETRIEVE_URL = API_URL + 'get'
    MODIFY_URL = API_URL + 'send'
