from pyramid.view import view_config
from pyramid.response import Response
import transaction
from datetime import datetime, timedelta

from sqlalchemy.exc import DBAPIError

from .. import models
from ..models import RecordModel
from ..utils.time_utils import today22h, today10h, refresh


@view_config(route_name='home', renderer='../templates/main.jinja2')
def default(request):
    refresh(request)
    lists = get_lists(request)
    return {'try': False, 'lists': lists}


@view_config(route_name='register', renderer='../templates/main.jinja2')
def register(request):
    lists = get_lists(request)
    if "service" in request.params:
        serv_type = int(request.params["service"])

        record = None
        records = request.dbsession.query(models.RecordModel).filter_by(room=serv_type).all()
        if len(records) != 0:
            last_record = records[-1]
            if last_record.time + timedelta(minutes=5) < today22h():
                record = add_record(request, serv_type, last_record.time + timedelta(minutes=5))
        else:
            if datetime.now(tz=None) < today10h():
                record = add_record(request, serv_type, today10h())
            elif datetime.now(tz=None) < today22h():
                record = add_record(request, serv_type, datetime.now(tz=None))

        lists = get_lists(request)
        return {'try': True, 'success': record is not None,
                'record': record, 'lists': lists, 'number': len(records) + 1}
    else:
        return {'try': False, 'lists': lists}


def get_lists(request):
    res = []
    for i in range(3):
        res.append(request.dbsession.query(models.RecordModel).filter_by(room=i).all())
    return res


def add_record(request, stype, time):
    record = RecordModel(room=stype, time=time)
    request.dbsession.add(record)
    transaction.commit()
    return record
