"""
:created on: 2017-09-01

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""
import logging

from django.core.exceptions import ValidationError
from django.db.models.fields import IntegerField, FloatField

from services.hyg import HYGService
from .models import Star


log = logging.getLogger('fill_db')


class FillDB(object):
    @classmethod
    def fill_db(cls):
        log.info('Database filling started.')
        data = HYGService.parse_csv()  # fixme: get_data is more suitable name
        for line in data:
            f_line = cls._filter_lines(line)
            cls._save_to_db(f_line)
        log.info('Database filling ended')

    @staticmethod
    def _save_to_db(line):
        try:
            s = Star(**line)
            s.clean_fields()
        except ValidationError as e:
            log.debug('{}: {}'.format(e, line))
        else:
            s.save()

    @staticmethod
    def _filter_lines(line):
        results = {}
        for field, value in line.items():  # fixme: this is uglyyyy
            if field == 'id':
                continue
            f = Star._meta._forward_fields_map.get(field, None)
            if not f:
                continue
            if isinstance(f, FloatField):
                try:
                    results[field] = float(value)
                except ValueError:
                    results[field] = None
            elif isinstance(f, IntegerField):
                try:
                    results[field] = int(value)
                except ValueError:
                    results[field] = None
            else:
                results[field] = value
        return results
