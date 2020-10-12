from app.models.base import Base


class Resource(Base):
    """
    Resources available
    """
    resources: list = []
    current_id: int = 0

    def __init__(self, name: str):
        super().__init__()
        self.name: str = name

    @staticmethod
    def create(name: str):
        """
        Create resource
        :param name: resource name
        :return: Resource object created
        """
        resource: Resource = Resource(name)
        Resource.resources.append(resource)
        return resource

    @classmethod
    def get_resource(cls, name):
        """
        Get resource based on given name
        :param name: resource name
        :return: Resource object
        """
        for resource in cls.resources:
            if resource.name == name:
                return resource
