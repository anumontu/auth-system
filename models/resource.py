from models.base import Base


class Resource(Base):
    resources: list = []
    current_id: int = 0

    def __init__(self, name: str):
        super().__init__()
        self.name: str = name

    @staticmethod
    def create(name: str):
        resource: Resource = Resource(name)
        Resource.resources.append(resource)
        return resource

    @classmethod
    def get_resource(cls, name):
        for resource in cls.resources:
            if resource.name == name:
                return resource
