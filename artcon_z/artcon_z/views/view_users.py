from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from ..models.services.user_type_record import UserTypeRecordService
from ..models.services.user_record import UserRecordService

@view_config(route_name='view_users', renderer='artcon_z:templates/view_users.pt')
def view_users(request):
    user_type_id = request.matchdict['user_type_id']
    print 'User type id is: ', user_type_id
    user_type = UserTypeRecordService.by_id(user_type_id) # DBSession.query(UserType).filter_by(id=user_type_id).first()
    users = UserRecordService.by_user_type(user_type_id) # DBSession.query(User).filter_by(user_type_id=user_type_id).all()
    if not users:
        return HTTPFound(location=request.route_url('add_user', user_type_id=user_type_id))
    return dict(users=users, user_type=user_type, logged_in=request.authenticated_userid)