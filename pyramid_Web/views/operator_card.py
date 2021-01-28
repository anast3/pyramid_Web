import transaction
from pyramid.view import view_config
from .. import models
from ..models import CardModel


@view_config(route_name='admin/card', renderer='../templates/cards.jinja2')
def default_consult(request):
    list_queue = request.dbsession.query(models.RecordModel).filter_by(room=0).all()
    list_cards = request.dbsession.query(models.CardModel).all()
    return {'list_queue': list_queue,
            'list_cards': list_cards}


@view_config(route_name='admin/card_close', renderer='../templates/cards.jinja2')
def remove_consult(request):
    id_ = request.params["id"]
    request.dbsession.query(models.RecordModel).filter_by(id=id_).delete()
    card = CardModel(number=request.params["num"],
                     validity=request.params["val"],
                     client_id=request.params["name"])
    request.dbsession.add(card)
    transaction.commit()
    list_queue = request.dbsession.query(models.RecordModel).filter_by(room=0).all()
    list_cards = request.dbsession.query(models.CardModel).all()
    return {'list_queue': list_queue,
            'list_cards': list_cards}
