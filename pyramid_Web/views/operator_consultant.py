from pyramid.view import view_config
from .. import models


@view_config(route_name='admin/consult/queue', renderer='../templates/consultations.jinja2')
def default_consult(request):
    list_ = get_lists(request)
    return {'list': list_}


@view_config(route_name='admin/consult/close', renderer='../templates/consultations.jinja2')
def remove_consult(request):
    id_ = request.params["id"]
    request.dbsession.query(models.RecordModel).filter_by(id=id_).delete()
    list_ = get_lists(request)
    return {'list': list_}


def get_lists(request):
    return request.dbsession.query(models.RecordModel).filter_by(room=2).all()
