from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from ..models.meta import DBSession
from ..models.services.user_type_record import UserTypeRecordService

@view_config(route_name='add_user', renderer='artcon_z:templates/edit.pt', permission='edit')
def add_user(request):
    user_type_id = request.matchdict['user_type_id']
    print '********************** Comes Here ', user_type_id,'**********************'
    # name = request.matchdict['name']
    if 'form.submitted' in request.params:
        name = request.params['name']
        user_type_id = request.params['user_type']
        user = User(name=name, user_type_id=user_type_id)
        print 'User: ', user.name, ' is a ', user_type_id
        DBSession.add(user)
        print 'User: ', user.name, ' has id ', user.id
        return HTTPFound(location=request.route_url('view_user',
                                                        user_id=user.id))
    user_types = UserTypeRecordService.all() # DBSession.query(UserType).all()
    save_url = request.route_url('add_user', user_type_id=user_type_id)
    return dict(
        user_types=user_types, 
        user_type_id=user_type_id, 
        save_url=save_url, 
        user=None, 
        logged_in=request.authenticated_userid
        )