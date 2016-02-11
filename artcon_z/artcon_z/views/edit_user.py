from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from ..models.meta import DBSession
from ..models.services.user_type_record import UserTypeRecordService
from ..models.services.user_record import UserRecordService

@view_config(route_name='edit_user', renderer='artcon_z:templates/edit.pt', permission='edit')
def edit_user(request):
    print 'CAME HERE BRAH'
    user_id = request.matchdict['user_id']
    user = UserRecordService.by_id(user_id) # DBSession.query(User).filter_by(id=user_id).one()
    if 'form.submitted' in request.params:
        user.user_type_id = request.params['user_type']
        user.name = request.params['name']
        DBSession.add(user)
        return HTTPFound(location=request.route_url('view_user',
                                                    user_id=user.id))
    user_types = UserTypeRecordService.all() # DBSession.query(UserType).all()
    return dict(
        user_types=user_types,
        user_type_id=user.user_type_id,
        user=user,
        save_url=request.route_url('edit_user',user_id=user.id), 
        logged_in=request.authenticated_userid
        )