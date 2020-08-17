#!/usr/bin/env python3

import connexion
import os
from communication_module import encoder
from dbhandler.mysql_handler import MySQLHandler

def main():
    print('communication-service-component v1: ' + os.environ['INIT'])
    # init db
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Communication.ai API'}, pythonic_params=True)
    app.run(port=80)


if __name__ == '__main__':
    main()
