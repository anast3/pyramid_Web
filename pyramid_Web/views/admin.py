from pyramid.view import view_config


@view_config(route_name='admin', renderer='../templates/admin.jinja2')
def admin(request):
    return {}
