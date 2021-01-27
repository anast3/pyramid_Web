def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('register', '/register')
    config.add_route('admin/consult/queue', '/admin/consult/queue')
    config.add_route('admin/consult/close', '/admin/consult/close')
    config.add_route('admin/card/queue', '/admin/card/queue')
    config.add_route('admin/card/close', '/admin/card/close')
