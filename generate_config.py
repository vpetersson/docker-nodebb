#!/usr/bin/env python

import os
import json
import sys

CONFIG = {}
SECRET = os.getenv('SECRET', False)
DBSERVERS = os.getenv('DBSERVERS', False)
DBPORT = 27017
CONFIGFILE = '/opt/nodebb/config.json'


if not (SECRET and DBSERVERS):
    print 'Missing SECRET or DBSERVERS environment variable. Exiting.'
    sys.exit(1)


def port_list():
    ports = []
    for p in DBSERVERS.split(','):
        ports.append(str(DBPORT))
    return ','.join(ports)


CONFIG['url'] = 'http://0.0.0.0:4567'
CONFIG['secret'] = SECRET
CONFIG['database'] = 'mongo'
CONFIG['mongo'] = {
    'host': ','.join(DBSERVERS.split(',')),
    'port': port_list(),
    'username': '',
    'password': '',
    'database': 'nodebb'
}

with open(CONFIGFILE, 'w') as f:
    f.write(json.dumps(CONFIG))
