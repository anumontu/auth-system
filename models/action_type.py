from enum import Enum


class ActionType(Enum):
    READ = 'READ'
    WRITE = 'WRITE'
    DELETE = 'DELETE'
