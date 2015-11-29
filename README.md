Lightweight Django Project in Docker
====================================

Based on https://docs.docker.com/compose/django/

After creating the files:
  Dockerfile
  django-compose.yml
  requirements.txt
  
From the directory with the Dockerfile issue this command:

$ docker-compose run web django-admin.py startproject composeexample .

This will create the composeexample directory as root:root, so:

sudo chown -R $USER:$USER .



