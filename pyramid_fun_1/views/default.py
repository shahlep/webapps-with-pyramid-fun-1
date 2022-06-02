from pyramid.view import view_config


@view_config(route_name="home", renderer="pyramid_fun_1:templates/mytemplate.pt")
def my_view(request):
    return {"project": "pyramid_fun_1"}
