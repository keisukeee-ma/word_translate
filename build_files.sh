#!/bin/bash
pip install -r requirements_vercel.txt
python manage.py collectstatic --noinput
