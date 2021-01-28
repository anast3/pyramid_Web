from pyramid.view import view_config
from .. import models


@view_config(route_name='admin/consult', renderer='../templates/consultations.jinja2')
def default_consult(request):
    return {'list': request.dbsession.query(models.RecordModel).filter_by(room=2).all()}


@view_config(route_name='admin/consult_close', renderer='../templates/consultations.jinja2')
def remove_consult(request):
    id_ = request.params["id"]
    request.dbsession.query(models.RecordModel).filter_by(id=id_).delete()
    list_ = request.dbsession.query(models.RecordModel).filter_by(room=2).all()
    return {'list': list_}
