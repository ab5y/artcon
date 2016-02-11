import os
import sys
from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from sqlalchemy import engine_from_config

from .models.meta import (
    DBSession,
    Base,
    user_pwd_context,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    basepath = os.path.dirname(__file__)
    filepath = os.path.abspath(os.path.join(basepath, "..", "development.ini"))
    print filepath
    user_pwd_context.load_path(filepath)
    

    authn_policy = AuthTktAuthenticationPolicy(
        'noctra', hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()

    config = Configurator(settings=settings,
                            root_factory='artcon_z.models.RootFactory')
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('view_user_types', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('register', '/register')
    config.add_route('view_users','/{user_type_id}')
    config.add_route('view_user', '/view_user/{user_id}')
    config.add_route('add_user','/{user_type_id}/add_user')
    config.add_route('edit_user','/{user_id}/edit_user', factory='artcon_z.security.UserFactory', 
                        traverse='/{user_id}')
    config.scan()
    return config.make_wsgi_app()
