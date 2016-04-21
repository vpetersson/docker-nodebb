#!/bin/bash
set -ex

/opt/bin/generate_config.py

cd /opt/nodebb
npm start
