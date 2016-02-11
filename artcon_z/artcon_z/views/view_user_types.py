from pyramid.view import (
    view_config,
    forbidden_view_config,
    )

from ..models.services.user_type_record import UserTypeRecordService

@view_config(route_name='view_user_types', renderer='artcon_z:templates/view_usertypes.pt', permission='view')
def view_user_types(request):
    # Home page displays three types of Users to view
    user_types = UserTypeRecordService.all()
    return dict(user_types=user_types, logged_in=request.authenticated_userid)