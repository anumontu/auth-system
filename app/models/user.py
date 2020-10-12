import hashlib

from app.models.base import Base


class User(Base):
    """
    User model
    """
    users: list = []
    logged_in_user = None
    current_id: int = 0

    def __init__(self, first_name: str, last_name: str, email: str, password: str, is_admin: bool = False):
        super().__init__()
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.email: str = email
        self.password: str = self.hash_password(password)
        self.is_admin: bool = is_admin

    @staticmethod
    def hash_password(password: str):
        """
        Utility for user's password hashing
        :param password: Password string
        :return: Hashed password
        """
        return hashlib.md5(bytes(password, encoding='utf8')).hexdigest()

    @staticmethod
    def create(first_name: str, last_name: str, email: str, password: str, is_admin: bool = False):
        """
        Create user
        :param first_name: User's first name
        :param last_name: User's last name
        :param email: User's email
        :param password: User's password
        :param is_admin: Should this user be admin ?
        :return: User object created
        """
        user: User = User(first_name, last_name, email, password, is_admin=is_admin)
        User.users.append(user)
        return user

    @classmethod
    def get_user(cls, email: str):
        """
        Get user based on email
        :param email: User's email
        :return: User object
        """
        for user in cls.users:
            if user.email == email:
                return user

    @classmethod
    def get_users(cls, is_admin: bool):
        """
        Get users (Admin/Normal User)
        :param is_admin: bool to get admin users or normal users
        :return: List of users
        """
        return [user for user in cls.users if user.is_admin == is_admin]

    def verify_password(self, password):
        """
        Utility for verifying user's password
        :param password: Input password
        :return: True if password is correct otherwise false
        """
        return self.password == self.hash_password(password)
