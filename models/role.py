from models.base import Base
from models.user import User


class Role(Base):
    roles: list = []
    current_id: int = 0

    def __init__(self, name: str):
        super().__init__()
        self.name: str = name

    @staticmethod
    def create(name: str):
        role: Role = Role(name)
        Role.roles.append(role)
        return role
