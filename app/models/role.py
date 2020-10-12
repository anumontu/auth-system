from app.models.base import Base


class Role(Base):
    """
    Roles that be associated with a user
    """
    roles: list = []
    current_id: int = 0

    def __init__(self, name: str):
        super().__init__()
        self.name: str = name

    @staticmethod
    def create(name: str):
        """
        Create role
        :param name: role name
        :return: Role object created
        """
        role: Role = Role(name)
        Role.roles.append(role)
        return role
