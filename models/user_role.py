from models.base import Base
from models.role import Role
from models.user import User


class UserRole(Base):
    user_roles: list = []
    current_id: int = 0

    def __init__(self, user: User, role: Role):
        super().__init__()
        self.user: User = user
        self.role: Role = role

    @staticmethod
    def create(user: User, role: Role):
        user_role: UserRole = UserRole(user, role)
        UserRole.user_roles.append(user_role)
        return user_role

    @classmethod
    def get_user_roles(cls, user: User):
        return [user_role for user_role in cls.user_roles if user_role.user.id == user.id]

    @classmethod
    def get_roles(cls, user: User):
        return [user_role.role for user_role in cls.user_roles if user_role.user.id == user.id]

    @classmethod
    def get_other_roles(cls, user: User):
        current_roles = cls.get_roles(user)
        return [role for role in Role.roles if role not in current_roles]
