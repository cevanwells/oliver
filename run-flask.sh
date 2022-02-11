#!/bin/sh

. env/bin/activate
exec gunicorn \
     --bind 0.0.0.0:5000 \
     --access-logfile /home/logs/access.log \
     --error-logfile /home/logs/error.log \
     wsgi:app
