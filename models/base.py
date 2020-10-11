from datetime import datetime


class Base:
    @classmethod
    def get_next_id(cls):
        cls.current_id += 1
        return cls.current_id

    def __init__(self):
        self.id: int = self.get_next_id()
        self.active: bool = True
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()

    def __str__(self):
        return self.__dict__

    def __repr__(self):
        return str(self.__dict__)
