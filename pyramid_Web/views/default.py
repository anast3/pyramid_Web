from pyramid.view import view_config
from pyramid.response import Response
import transaction
from datetime import datetime, timedelta

from sqlalchemy.exc import DBAPIError

from .. import models
from ..models import RecordModel
from ..utils.time_utils import today18h


@view_config(route_name='home', renderer='../templates/main.jinja2')
def default(request):
    lists = get_lists(request)
    return {'try': False, 'lists': lists}


@view_config(route_name='register', renderer='../templates/main.jinja2')
def register(request):
    success = False
    serv_type = int(request.params["service"])

    records = request.dbsession.query(models.RecordModel).filter_by(room=serv_type).all()
    if len(records) != 0:
        last_record = records[-1]
        if last_record.time + timedelta(minutes=30) < today18h():
            record = RecordModel(room=serv_type, time=last_record.time + timedelta(minutes=30))
            request.dbsession.add(record)
            transaction.commit()
            success = True
    else:
        record = RecordModel(room=serv_type, time=datetime.now(tz=None))
        request.dbsession.add(record)
        transaction.commit()

    lists = get_lists(request)
    return {'try': True, 'success': success, 'record': record, 'lists': lists}


def get_lists(request):
    res = []
    for i in range(3):
        res.append(request.dbsession.query(models.RecordModel).filter_by(room=i).all())
    return res


