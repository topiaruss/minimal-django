#!/usr/bin/env bash

openssl req -new -newkey rsa:2048 -days 1000 -nodes -x509 -keyout dev.minimal-django.net.key -out dev.minimal-django.net.crt


