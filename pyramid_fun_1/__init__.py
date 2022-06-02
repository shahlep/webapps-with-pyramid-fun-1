from pyramid.config import Configurator


def main(global_config, **settings):
    """This function returns a Pyramid WSGI application."""
    with Configurator(settings=settings) as config:
        config.include("pyramid_chameleon")
        config.add_static_view("static", "static", cache_max_age=3600)
        config.add_route("home", "/")
        config.add_route("about", "/about")
        config.scan()
    return config.make_wsgi_app()
