from app.models.action_type import ActionType
from app.models.resource import Resource
from app.models.role import Role
from app.models.role_resource import RoleResource
from app.models.user import User
from app.models.user_role import UserRole


class Setup:
    """
    Initial setup for the system
    """

    def init(self):
        """
        Setup data
        """
        user: User = self.init_users()
        self.init_resources(user)

    @staticmethod
    def init_users():
        """
        Create user data
        :return: A normal user created
        """
        User.create('Anubhav', 'Verma', 'anubhavverma@gmail.com', 'anumontu', is_admin=True)
        user: User = User.create('Ananya', 'Verma', 'ananyaverma@gmail.com', 'anni')
        return user

    @staticmethod
    def init_resources(user: User):
        """
        Create resources data and associate it with a user
        :param user: User object
        """
        resource: Resource = Resource.create('User')
        Setup.init_role(resource)
        resource: Resource = Resource.create('Image')
        role: Role = Setup.init_role(resource)
        Setup.init_user_role(user, role)
        resource: Resource = Resource.create('Pdf')
        Setup.init_role(resource)

    @staticmethod
    def init_role_resource(role: Role, resource: Resource, action_type: ActionType):
        """
        Create Role and Resource mapping
        :param role: Role object
        :param resource: Resource mapping
        :param action_type: Action Type
        """
        RoleResource.create(role, resource, action_type)

    @staticmethod
    def init_role(resource: Resource):
        """
        Create roles and associate it with a resource
        :param resource: Resource object
        :return: Edit Role for a resource
        """
        role: Role = Role.create(f'Read {resource.name}')
        Setup.init_role_resource(role, resource, ActionType.READ)
        role: Role = Role.create(f'Edit {resource.name}')
        Setup.init_role_resource(role, resource, ActionType.WRITE)
        Setup.init_role_resource(role, resource, ActionType.DELETE)
        return role

    @staticmethod
    def init_user_role(user: User, role: Role):
        """
        Create User and Role mapping
        :param user: User object
        :param role: Role object
        """
        UserRole.create(user, role)
