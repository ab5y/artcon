from docutils.core import publish_parts
from pyramid.view import view_config

from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
    )

from ..models.services.user_record import UserRecordService

@view_config(route_name='view_user', renderer='artcon_z:templates/view.pt', permission='view')
def view_user(request):
    print '********************** Comes Here 1**********************'
    user_id = request.matchdict['user_id']
    user = UserRecordService.by_id(user_id) # DBSession.query(User).filter_by(id=user_id).first()
    if user is None:
        return HTTPNotFound('No such page')

    content = publish_parts(user.name, user.user_type_id, writer_name='html')['html_body']
    edit_url = request.route_url('edit_user', user_id=user_id)
    return dict(
        user=user, 
        content=content, 
        edit_url=edit_url, 
        logged_in=request.authenticated_userid
        )