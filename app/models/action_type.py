from enum import Enum


class ActionType(Enum):
    """
    Available action types to be performed on a resource
    """
    READ = 'READ'
    WRITE = 'WRITE'
    DELETE = 'DELETE'
