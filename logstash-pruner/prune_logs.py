#!/usr/bin/python3

import datetime
import os
import requests
import sys

if sys.version_info[0] >= 3:
    import urllib.parse as urllib
else:
    import urllib

endpoint = os.environ['ELASTICSEARCH_URL']
username = os.environ['ELASTICSEARCH_USERNAME']
password = os.environ['ELASTICSEARCH_PASSWORD']
prune_start = datetime.datetime.utcnow() - datetime.timedelta(days=60)

r = requests.get('{0}/_cat/indices'.format(endpoint),
                 auth=(username, password))
for line in r.text.splitlines():
    data = line.split(' ')
    if len(data) > 10:
        index = data[2]
        indexd = index.split('-')
        if len(indexd) > 1:
            d = datetime.datetime.strptime(indexd[1], "%Y.%m.%d")
            if d < prune_start:
                r2 = requests.delete(
                    '{0}/{1}'.format(endpoint, urllib.quote(index)),
                    auth=(username, password))
                print(index, r2.json())
