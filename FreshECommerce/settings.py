"""
Django settings for FreshECommerce project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))
sys.path.insert(0, os.path.join(BASE_DIR, "extra_apps"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-%(4$9d7nhd(yi(r86d004pu7asr7sl2gq)xd)0shm&&p@2$**("

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = "users.UserProfile"


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "users.apps.UsersConfig",
    # "goods",
    # "trade",
    # "user_operation",
    "goods.apps.GoodsConfig",
    "trade.apps.TradeConfig",
    "user_operation.apps.UserOperationConfig",
    "DjangoUeditor",
    "xadmin",
    "crispy_forms",
    'crispy_bootstrap3', # 安装crispy-bootstrap3第三方依赖包
    # DRF配置
    "rest_framework",
    # 自动生成API文档
    "drf_yasg",
    # 精确搜索
    "django_filters",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "FreshECommerce.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "FreshECommerce.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "fresh_es",
        "HOST": "127.0.0.1",  # 数据库地址，本机 ip 地址 127.0.0.1
        "PORT": 3306,  # 端口
        "USER": "root",  # 数据库用户名
        "PASSWORD": "123456",  # 数据库密码
        # 因为第三方登录时需要进行数据迁移，需要添加 OPTIONS 参数， MySQL 数据库引擎设置存储引擎为 INNODB，否则会报错
        # "OPTIONS": {"init_command": "SET default_storage_engine = INNODB;"},
        # 默认引擎是不是INNODB 不用配置
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# LANGUAGE_CODE = "en-us"
LANGUAGE_CODE = "zh-hans"  # 中文支持

# TIME_ZONE = "UTC"
TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

# 用于控制是否启用本地化（Localization）功能
USE_L10N = True

# USE_TZ = True
# 用于控制是否启用时区支
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# 静态资源设置
STATIC_URL = "static/"

# 媒体资源设置
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# DRF全局配置
REST_FRAMEWORK = {
    # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    # "PAGE_SIZE": 10,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.AutoSchema",
    # 格式化time
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S",
}
