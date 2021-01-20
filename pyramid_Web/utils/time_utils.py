from datetime import datetime, timedelta
from .. import models

def today18h():
    today = datetime.today()
    midnight = datetime(today.year, today.month, today.day)
    return midnight + timedelta(hours=18)


def today10h():
    today = datetime.today()
    midnight = datetime(today.year, today.month, today.day)
    return midnight + timedelta(hours=10)


def isBefore(time):
    return time < datetime.now(tz=None)


def refresh(request):
    request.dbsession.query(models.RecordModel).filter(isBefore(models.RecordModel.time)).delete()
