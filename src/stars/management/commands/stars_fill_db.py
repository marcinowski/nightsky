"""
:created on: 2017-09-01

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""
from django.core.management import BaseCommand
from ...services import FillDB


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        FillDB.fill_db()
