from jediacademy.settings.base import *

DEBUG = True

ALLOWED_HOSTS += ['*', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jediacademy',
        'USER': 'jedidjango',
        'PASSWORD': 'masterkey',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

"""
email
"""

ADMINS = [
    ('vlad', 'yetanothersitemail@gmail.com'),
]

MANAGERS = [
    ('vlad', 'yetanothersitemail@gmail.com'),
]

SERVER_EMAIL = 'yetanothersitemail@gmail.com'

DEFAULT_FROM_EMAIL = 'postmaster@appd2cb3ded4cdf448c8c29b5d31a03d4b1.mailgun.org'

EMAIL_HOST = 'smtp.mailgun.org'

EMAIL_PORT = 465

EMAIL_USE_SSL = True

EMAIL_HOST_USER = 'postmaster@appd2cb3ded4cdf448c8c29b5d31a03d4b1.mailgun.org'

EMAIL_HOST_PASSWORD = 'e174d564f9ebf115e74636f58e4ff15c'

ADMIN_SITE_HEADER = 'JediAcademy'

INTERNAL_IPS = ['127.0.0.1', ]
