# flask_api

flask_api is a simple API and was created to make setting up wsgi easy.

This repository used docker and ubuntu 16.04, python3, flask.

If you want to develop and add a Python library, you can save it in libs and call it from run.py.



## useage

Here are two ways to use flask_api.

1. image build & run & stop

   `docker build -t flask_api .`

    `docker run -d -p 80:80 --name {name} flask_api`

    `docker stop {name}`

2. docker-compose

   `docker-compose up -d`

   `docker-compose down`

