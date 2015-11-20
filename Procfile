web: gunicorn suitegenius.wsgi_$ENV --log-file -
worker: DJANGO_SETTINGS_MODULE=suitegenius.settings.$ENV rqworker -c rq_settings.$ENV