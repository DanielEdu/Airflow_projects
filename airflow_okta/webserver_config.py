import os
from flask_appbuilder.security.manager import AUTH_OAUTH


AUTH_TYPE = AUTH_OAUTH
OAUTH_PROVIDERS = [
{'name': 'okta', 'icon': 'fa-circle-o',
        'token_key': 'access_token',
        'remote_app': {
            'client_id': '0oa67in04ipqo60Dq696',
            'client_secret': '',
            'api_base_url': 'https://  .okta.com/oauth2/v1/',
            'client_kwargs': {
                'scope': 'openid profile email groups'
            },
            'access_token_url': 'https://  .okta.com/oauth2/v1/token',
            'authorize_url': 'https://  .okta.com/oauth2/v1/authorize',
    }
    }
]

