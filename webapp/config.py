from datetime import timedelta
import os

basedir = os.path.abspath(os.path.dirname(__file__))


WEATHER_DEFAULT_CITY = "Moscow, Russia"
WEATHER_API_KEY = "9f697681e7584dc59a6151015190506"
WEATHER_URL = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')

SQLALCHEMY_TRACK_MODIFICATIONS = False

REMEMBER_COOKIE_DURATION = timedelta(days=5)

SECRET_KEY = 'VERY_SECRET_KEY'
from webapp.config_local import *