release: sh -c 'cd uc && python manage.py collectstatic && python manage.py migrate'
web: sh -c 'cd uc && gunicorn uc.wsgi --log-file -'