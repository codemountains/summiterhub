import os
import environ

# 本番環境用設定ファイル
try:
	from .settings_core import *
except ImportError:
	pass

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

# SECRET KEY
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# CORS_ORIGIN_WHITELIST

CORS_ORIGIN_WHITELIST = [
	'http://localhost:3000',
]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
	'default': env.db(),
}

# Email backend

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

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
			'level': 'INFO',
		}
	},

	# ハンドラの設定
	'handlers': {
		'console': {
			'level': 'INFO',
			'class': 'logging.TimedRotatingFileHandler',
			'filename': os.path.join(BASE_DIR, 'logs/django.log'),
			'formatter': 'prod',
			'when': 'D',
			'interval': 1,
			'backupCount': 7,
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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media

MEDIA_ROOT = Path(BASE_DIR, 'media')

MEDIA_URL = '/media/'
