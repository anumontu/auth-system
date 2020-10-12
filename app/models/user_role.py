from app.models.base import Base
from app.models.role import Role
from app.models.user import User


class UserRole(Base):
    """
    Through model between User and Role
    """
    user_roles: list = []
    current_id: int = 0

    def __init__(self, user: User, role: Role):
        super().__init__()
        self.user: User = user
        self.role: Role = role

    @staticmethod
    def create(user: User, role: Role):
        """
        Create User and Role mapping
        :param user: User object
        :param role: Role object
        :return: UserRole object created
        """
        user_role: UserRole = UserRole(user, role)
        UserRole.user_roles.append(user_role)
        return user_role

    @classmethod
    def get_user_roles(cls, user: User):
        """
        Get list of UserRoles associated with a particular user
        :param user: User object
        :return: List of UserRoles
        """
        return [user_role for user_role in cls.user_roles if user_role.user.id == user.id]

    @classmethod
    def get_roles(cls, user: User):
        """
        Get list of roles associated with a particular user
        :param user: User object
        :return: List of roles
        """
        return [user_role.role for user_role in cls.user_roles if user_role.user.id == user.id]

    @classmethod
    def get_other_roles(cls, user: User):
        """
        Get list of roles not associated with the current user
        :param user: User object
        :return: List or roles
        """
        current_roles = cls.get_roles(user)
        return [role for role in Role.roles if role not in current_roles]
