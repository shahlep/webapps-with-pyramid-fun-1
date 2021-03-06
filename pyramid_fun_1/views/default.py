from pyramid.view import view_config


def get_test_packages():
    return [
        {"name": "robotframework", "version": "5.0.0"},
        {"name": "requests", "version": "1.2.3"},
        {"name": "playwright", "version": "1.22"},
    ]


@view_config(route_name="home", renderer="pyramid_fun_1:templates/home_index.pt")
def home_index(_):
    return {"project": get_test_packages()}


@view_config(route_name="about", renderer="pyramid_fun_1:templates/home_about.pt")
def home_about(_):
    return {}
