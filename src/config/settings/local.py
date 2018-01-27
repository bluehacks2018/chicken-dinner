from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+&w*)pv8lw2v3-e)9o+6bk-(2i%umfv0_^@4-6d9=nfdh9s=@e'

#SECURITY WARNING: Debug is turned on for local development only
DEBUG = env.bool('DJANGO_DEBUG', default=True)

ALLOWED_HOSTS = [
    'web',
    'localhost',
]
