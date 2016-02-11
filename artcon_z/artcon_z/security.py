from pyramid.security import Allow, Everyone, Authenticated, ALL_PERMISSIONS
from artcon_z.models.services.user_record import UserRecordService

class UserFactory(object):
	__acl__ = [	(Allow, 'g:admin', ALL_PERMISSIONS) ]

	def __init__(self, request):
		self.request = request

	def __getitem__(self, key):
		user = UserRecordService.by_id(key)
		user.__parent__ = self
		user.__name__ = key
		return user