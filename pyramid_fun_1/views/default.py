from pyramid.view import view_config


@view_config(route_name="home", renderer="pyramid_fun_1:templates/home.pt")
def index(request):
    return {"project": "python packages index"}
