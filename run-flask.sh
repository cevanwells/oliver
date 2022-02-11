#!/bin/sh

source env/bin/activate
exec gunicorn --bind 0.0.0.0 wsgi:app