from models.action_type import ActionType
from models.resource import Resource
from models.role import Role
from models.role_resource import RoleResource
from models.user import User
from models.user_role import UserRole


class Setup:
    def init(self):
        user: User = self.init_users()
        self.init_resources(user)

    @staticmethod
    def init_users():
        User.create('Anubhav', 'Verma', 'anubhavverma@gmail.com', 'anumontu', is_admin=True)
        user: User = User.create('Ananya', 'Verma', 'ananyaverma@gmail.com', 'anni')
        return user

    @staticmethod
    def init_resources(user: User):
        resource: Resource = Resource.create('User')
        Setup.init_role(resource)
        resource: Resource = Resource.create('Image')
        role: Role = Setup.init_role(resource)
        Setup.init_user_role(user, role)
        resource: Resource = Resource.create('Pdf')
        Setup.init_role(resource)

    @staticmethod
    def init_role_resource(role: Role, resource: Resource, action_type: ActionType):
        RoleResource.create(role, resource, action_type)

    @staticmethod
    def init_role(resource: Resource):
        role: Role = Role.create(f'Read {resource.name}')
        Setup.init_role_resource(role, resource, ActionType.READ)
        role: Role = Role.create(f'Edit {resource.name}')
        Setup.init_role_resource(role, resource, ActionType.WRITE)
        Setup.init_role_resource(role, resource, ActionType.DELETE)
        return role

    @staticmethod
    def init_user_role(user: User, role: Role):
        UserRole.create(user, role)
