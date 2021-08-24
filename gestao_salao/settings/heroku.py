import environ

from gestao_salao.settings.base import *

env = environ.Env()

DEBUG=env.bool("DEBUG", True)
SECRET_KEY=env("SECRET_KEY")
ALLOWED_HOSTS=env.list("ALLOWED_HOSTS")
DATABASES={
    "default": env.db()
}