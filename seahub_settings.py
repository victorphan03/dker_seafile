# -*- coding: utf-8 -*-
SECRET_KEY = "m@wp7sn73@1%5wno#xf$-#8#qke)0imx(o#j6_9md$olb!^%47"
SERVICE_URL = "https://cloud.victorphan.net"

CSRF_TRUSTED_ORIGINS = [
    'https://cloud.victorphan.net',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seahub_db',
        'USER': 'seafile',
        'PASSWORD': '2ff2f120-0ba6-47d0-a6e3-5408e8a5dc0d',
        'HOST': 'db',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'LOCATION': 'memcached:11211',
    },
    'locmem': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}
COMPRESS_CACHE_BACKEND = 'locmem'
TIME_ZONE = 'Etc/UTC'
FILE_SERVER_ROOT = "https://cloud.victorphan.net/seafhttp"
