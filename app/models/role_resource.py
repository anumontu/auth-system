from app.models.action_type import ActionType
from app.models.base import Base
from app.models.resource import Resource
from app.models.role import Role


class RoleResource(Base):
    """
    Through model between Role and Resource
    """
    role_resources: list = []
    current_id: int = 0

    def __init__(self, role: Role, resource: Resource, action_type: ActionType):
        super().__init__()
        self.role: Role = role
        self.resource: Resource = resource
        self.action_type: ActionType = action_type

    @staticmethod
    def create(role: Role, resource: Resource, action_type: ActionType):
        """
        Create Role and Resource mapping
        :param role: Role object
        :param resource: Resource object
        :param action_type: Action Type object
        :return: RoleResource object created
        """
        role_resource: RoleResource = RoleResource(role, resource, action_type)
        RoleResource.role_resources.append(role_resource)
        return role_resource

    @classmethod
    def get_resources(cls, role: Role, action_type_name: str):
        """
        Get the resource associated with a particular role
        :param role: Role object
        :param action_type_name: Action type name
        :return: List of resources
        """
        return [role_resource.resource for role_resource in cls.role_resources if
                role_resource.role.id == role.id and role_resource.action_type.value == action_type_name]
