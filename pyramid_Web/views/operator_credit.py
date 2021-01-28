import transaction
from pyramid.view import view_config
from .. import models
from ..models import CreditModel


@view_config(route_name='admin/credit', renderer='../templates/credits.jinja2')
def default_consult(request):
    list_queue = request.dbsession.query(models.RecordModel).filter_by(room=1).all()
    list_credits = request.dbsession.query(models.CreditModel).all()
    return {'list_queue': list_queue,
            'list_credits': list_credits}


@view_config(route_name='admin/close_credit', renderer='../templates/credits.jinja2')
def remove_consult(request):
    id_ = request.params["id"]
    request.dbsession.query(models.RecordModel).filter_by(id=id_).delete()
    credit = CreditModel(amount=request.params["sum"],
                         validity=request.params["val"],
                         client_id=request.params["name"],
                         percent=request.params["per"])
    request.dbsession.add(credit)
    transaction.commit()
    list_queue = request.dbsession.query(models.RecordModel).filter_by(room=1).all()
    list_credits = request.dbsession.query(models.CreditModel).all()
    return {'list_queue': list_queue,
            'list_credits': list_credits}
