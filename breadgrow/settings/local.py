from .base import *

# 로컬 설정파일
def read_secret(secret_name):
    file =open('/run/secrets/' +secret_name)
    secret =file.read()
    secret =secret.rstrip().lstrip()
    file.close()

    return secret


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)



# Take environment variables from .env file
# environ.Env.read_env(os.path.join(BASE_DIR, '../../.env'))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))






# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8000/']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}