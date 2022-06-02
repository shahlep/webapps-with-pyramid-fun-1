from pyramid.view import view_config


@view_config(route_name="home", renderer="pyramid_fun_1:templates/home_index.pt")
def home_index(request):
    return {"project": "python packages index"}
