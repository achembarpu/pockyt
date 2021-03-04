from __future__ import absolute_import, print_function, unicode_literals, with_statement


class API(object):
    """
    Pocket API Access Data
    """

    APP_NAME = "pockyt"

    POCKET_URL = "https://getpocket.com"
    API_URL = POCKET_URL + "/v3"

    REDIRECT_URL = "https://www.github.com/achembarpu/{0}".format(APP_NAME)
    ISSUE_URL = REDIRECT_URL + "/issues/new"
    APP_CREATE_URL = "http://getpocket.com/developer/apps/new"

    REQUEST_TOKEN_URL = API_URL + "/oauth/request"
    ACCESS_TOKEN_URL = API_URL + "/oauth/authorize"

    RETRIEVE_URL = API_URL + "/get"
    MODIFY_URL = API_URL + "/send"

    CONFIG_HEADER = "CREDENTIALS"

    ENCODING = "utf-8"
    DECODING = "unicode_escape"

    CONTENT_TYPE = "application/json"

    INFO_KEYS = ["id", "title", "link", "excerpt", "tags"]

    @classmethod
    def get_auth_user_url(cls, rt):
        return (cls.POCKET_URL + "/auth/authorize?request_token={0}"
                "&redirect_uri={1}".format(rt, cls.REDIRECT_URL))
