import os

# Import settings_core.py
try:
	from .settings_core import *
except ImportError:
	pass

# SECURITY WARNING: keep the secret key used in production secret!
# Import local settings.py
try:
	from .local_settings import *
except ImportError:
	pass

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# CORS_ORIGIN_WHITELIST

CORS_ORIGIN_WHITELIST = [
	'http://localhost:3000',
]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'summiterhub_dev',
		'USER': os.environ.get('DB_USER'),
		'PASSWORD': os.environ.get('DB_PASSWORD'),
	}
}

# Logging

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,

	# ロガーの設定
	'loggers': {
		# Djangoが利用するロガー
		'django': {
			'handlers': ['console'],
			'level': 'INFO',
		},
		# Dairyが利用するロガー
		'Diary': {
			'handlers': ['console'],
			'level': 'DEBUG',
		}
	},

	# ハンドラの設定
	'handlers': {
		'console': {
			'level': 'DEBUG',
			'class': 'logging.StreamHandler',
			'formatter': 'dev'
		},
	},

	# フォーマッタの設定
	'formatters': {
		'dev': {
			'format': '\t'.join([
				'%(asctime)s',
				'[%(levelname)s]',
				'%(pathname)s(Line:%(lineno)d)',
				'%(message)s'
			])
		},
	}
}
