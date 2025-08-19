# bookstore/settings.py

import os
from pathlib import Path
import environ  # Importe o environ

# --- INÍCIO DA CONFIGURAÇÃO DO ENVIRON ---
# Inicialize o environ
env = environ.Env(
    # Defina os tipos e valores padrão para as variáveis de ambiente
    DEBUG=(bool, False)
)

# O diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Leia o arquivo .env.dev (importante para o seu desenvolvimento local)
# O environ é inteligente e não vai dar erro se o arquivo não existir (como no GitHub Actions)
environ.Env.read_env(os.path.join(BASE_DIR, '.env.dev'))
# --- FIM DA CONFIGURAÇÃO DO ENVIRON ---


# Use as variáveis lidas pelo environ
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')

# 'DJANGO_ALLOWED_HOSTS' deve ser uma string de hosts separados por espaço no seu .env.dev
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['127.0.0.1', 'localhost', 'joaovictorangelo.pythonanywhere.com/'])


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "rest_framework",
    "order",
    "product",
    "debug_toolbar",
    "rest_framework.authtoken",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "bookstore.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "bookstore.wsgi.application"


# --- INÍCIO DA CONFIGURAÇÃO DO BANCO DE DADOS COM ENVIRON ---
# Esta é a correção principal.
# O env.db() lê a variável DATABASE_URL (que existe no GitHub Actions)
# Se não encontrar, ele usa um banco sqlite local como padrão.
DATABASES = {
    'default': env.db('DATABASE_URL', default=f'sqlite:///{BASE_DIR / "db.sqlite3"}')
}
# --- FIM DA CONFIGURAÇÃO DO BANCO DE DADOS COM ENVIRON ---


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
}

INTERNAL_IPS = ["127.0.0.1"]
