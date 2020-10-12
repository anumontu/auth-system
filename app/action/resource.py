from PyInquirer import prompt

from app.models.action_type import ActionType
from app.models.resource import Resource
from app.models.role_resource import RoleResource
from app.models.user import User
from app.models.user_role import UserRole
from app.util.common import input_style, Log


class ResourceActions:
    """
    Resource Actions to check if the current user has access to a particular resource
    """

    @staticmethod
    def has_access(user: User, resource_name: str, action_type_name: str):
        """
        Check if the giver user has access to perform the given action type on given resource
        :param user: User object
        :param resource_name: Resource name
        :param action_type_name: Action Type name
        :return: True if user has access otherwise False
        """
        for role in UserRole.get_roles(user):
            for resource in RoleResource.get_resources(role, action_type_name):
                if resource.name == resource_name:
                    return True
        return False

    @staticmethod
    def check_resource_access():
        """
        Check if the current user has access to perform an action on a particular resource
        """
        resource_names: list = [resource.name for resource in Resource.resources]
        if not resource_names:
            Log.log('No resources available available', color='red')
            return
        action_types: list = [action_type.value for action_type in ActionType]
        if not action_types:
            Log.log('No action types available', color='red')
            return
        choose_resource_questions: list = [
            {
                'type': 'list',
                'name': 'resource_name',
                'message': 'Choose Resource',
                'choices': resource_names
            },
            {
                'type': 'list',
                'name': 'access_type_name',
                'message': 'Choose Access Type',
                'choices': action_types
            }
        ]
        answers: dict = prompt(choose_resource_questions, style=input_style)
        if (User.logged_in_user.is_admin or
                ResourceActions.has_access(
                    User.logged_in_user, answers['resource_name'], answers['access_type_name']
                )):
            Log.log('Access Granted', color='green')
        else:
            Log.log('Access Denied', color='red')
