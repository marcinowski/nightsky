"""
:created on: 2017-09-01

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""
import csv
import gzip
import os
import requests
import shutil
from django.conf import settings


HYG_RESOURCE_URL = 'http://www.astronexus.com/files/downloads/hygdata_v3.csv.gz'
HYG_GZIP_FILE = 'hygdata.gz'
HYG_CSV_FILE = 'hygdata.csv'
HYG_GZIP_PATH = os.path.join(os.path.dirname(settings.BASE_DIR), 'resources', HYG_GZIP_FILE)
HYG_CSV_PATH = os.path.join(os.path.dirname(settings.BASE_DIR), 'resources', HYG_CSV_FILE)


class GetHYGData(object):

    def download_gz(self):
        with requests.get(HYG_RESOURCE_URL, stream=True) as r, open(HYG_GZIP_PATH, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    def unpack_gz(self):
        if not os.path.isfile(HYG_GZIP_PATH):
            raise OSError
        with gzip.open(HYG_GZIP_PATH, 'rb') as _gzip, open(HYG_CSV_PATH, 'w') as _csv:
            for line in _gzip:
                _csv.write(line.decode('utf-8'))

    def parse_csv(self):
        with open(HYG_CSV_PATH, 'r') as _csv:
            dict_r = csv.DictReader(_csv)
            result = [el for el in dict_r]
        return result
