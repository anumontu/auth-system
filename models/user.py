from models.base import Base
import hashlib


class User(Base):
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
        return hashlib.md5(bytes(password, encoding='utf8')).hexdigest()

    @staticmethod
    def create(first_name: str, last_name: str, email: str, password: str, is_admin: bool = False):
        user: User = User(first_name, last_name, email, password, is_admin=is_admin)
        User.users.append(user)
        return user

    @classmethod
    def get_user(cls, email: str):
        for user in cls.users:
            if user.email == email:
                return user

    @classmethod
    def get_users(cls, is_admin: bool):
        return [user for user in cls.users if user.is_admin == is_admin]

    def verify_password(self, password):
        return self.password == self.hash_password(password)
