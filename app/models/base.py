from datetime import datetime


class Base:
    """
    Base model for different entities
    """

    @classmethod
    def get_next_id(cls):
        """
        Get this next id that can be assigned to an object
        :return: next available id
        """
        cls.current_id += 1
        return cls.current_id

    def __init__(self):
        self.id: int = self.get_next_id()
        self.active: bool = True
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()
