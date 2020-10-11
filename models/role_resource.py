from models.action_type import ActionType
from models.base import Base
from models.resource import Resource
from models.role import Role


class RoleResource(Base):
    role_resources: list = []
    current_id: int = 0

    def __init__(self, role: Role, resource: Resource, action_type: ActionType):
        super().__init__()
        self.role: Role = role
        self.resource: Resource = resource
        self.action_type: ActionType = action_type

    @staticmethod
    def create(role: Role, resource: Resource, action_type: ActionType):
        role_resource: RoleResource = RoleResource(role, resource, action_type)
        RoleResource.role_resources.append(role_resource)
        return role_resource

    @classmethod
    def get_resources(cls, role: Role, action_type_name: str):
        return [role_resource.resource for role_resource in cls.role_resources if
                role_resource.role.id == role.id and role_resource.action_type.value == action_type_name]
