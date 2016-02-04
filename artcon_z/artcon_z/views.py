import cgi
import re
from docutils.core import publish_parts

from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
    )

# from pyramid.response import Response

from pyramid.view import view_config

# from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    UserType,
    User,
    )

@view_config(route_name='view_user_types', renderer='templates/view_usertypes.pt')
def view_user_types(request):
    # Home page displays three types of Users to view
    user_types = DBSession.query(UserType).all()
    return dict(user_types=user_types)

@view_config(route_name='view_users', renderer='templates/view_users.pt')
def view_users(request):
    print '********************** Comes Here 1**********************'
    user_type_id = request.matchdict['user_type_id']
    user_type = DBSession.query(UserType).filter_by(id=user_type_id).first()
    users = DBSession.query(User).all()
    if not users:
        return HTTPFound(location=request.route_url('add_user', user_type_id=user_type_id))
    return dict(users=users, user_type=user_type)

@view_config(route_name='view_user', renderer='templates/view.pt')
def view_user(request):
    user_id = request.matchdict['user_id']
    user = DBSession.query(User).filter_by(id=user_id).first()
    if user is None:
        return HTTPNotFound('No such page')

    content = publish_parts(user.name, user.user_type_id, writer_name='html')['html_body']
    edit_url = request.route_url('edit_user', user_id=user_id)
    return dict(user=user, content=content, edit_url=edit_url)

@view_config(route_name='add_user', renderer='templates/edit.pt')
def add_user(request):
    user_type_id = request.matchdict['user_type_id']
    print '********************** Comes Here ', user_type_id,'**********************'
    # name = request.matchdict['name']
    if 'form.submitted' in request.params:
        name = request.params['user.name']
        user_type_id = request.params['user.user_type']
        user = User(name=name, user_type_id=user_type_id)
        print 'User: ', user.name, ' is a ', user_type_id
        # DBSession.add(user)
        # return HTTPFound(location=request.route_url('view_user',
        #                                                 user_id=user.id))
    user_types = DBSession.query(UserType).all()
    save_url = request.route_url('add_user', user_type_id=user_type_id)
    return dict(user_types=user_types, user_type_id=user_type_id, save_url=save_url)

@view_config(route_name='edit_user', renderer='templates/edit.pt')
def edit_user(request):
    user_id = request.matchdict['user_id']
    user = DBSession.query(User).filter_by(id=user_id).one()
    if 'form.submitted' in request.params:
        user.user_type_id = request.params['user_type_id']
        user.name = request.params['name']
        DBSession.add(user)
        return HTTPFound(location=request.route_url('view_user',
                                                    user_id=user.id))
    return dict(
        user=user,
        save_url=request.route_url('edit_user',user_id=user.id)
        )