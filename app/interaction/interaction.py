from app.action.auth import Auth
from app.action.resource import ResourceActions
from app.action.role import RoleActions
from app.action.user import UserActions
from app.interaction.common import CommonInteraction
from app.models.user import User
from app.util.common import Log


class Interaction(CommonInteraction):

    def __init__(self):
        # Action common to a logged in user
        self.LOGGED_IN_ACTIONS: list = [
            {
                'message': 'Press 1 for login as another user',
                'action': Auth.login,
                'value': 1
            },
            {
                'message': 'Press 2 for access resource',
                'action': ResourceActions.check_resource_access,
                'value': 2
            },
        ]

        # Logout action
        self.LOGOUT_ACTIONS: list = [
            {
                'message': 'Press 0 for logout',
                'action': Auth.logout,
                'value': 0
            }
        ]

        # Actions for an admin
        self.ADMIN_ACTIONS: list = self.LOGGED_IN_ACTIONS + [
            {
                'message': 'Press 3 for create user',
                'action': UserActions.create_user,
                'value': 3
            },
            {
                'message': 'Press 4 for edit role',
                'action': RoleActions.edit_role,
                'value': 4
            }
        ] + self.LOGOUT_ACTIONS + super().ACTIONS

        # Actions for a normal user
        self.USER_ACTIONS: list = self.LOGGED_IN_ACTIONS + [
            {
                'message': 'Press 3 for view roles',
                'action': RoleActions.view_roles,
                'value': 3
            }
        ] + self.LOGOUT_ACTIONS + super().ACTIONS

        # Actions for a logged out user
        self.LOGGED_OUT_ACTIONS: list = [
                                            {
                                                'message': 'Press 1 for login',
                                                'action': Auth.login,
                                                'value': 1
                                            }
                                        ] + super().ACTIONS

    def get_actions(self):
        """
        Get actions available at a particular time base on logged in user(normal user/admin) or logged out user
        :return: List of actions
        """
        if User.logged_in_user:
            print('Hi! You are logged in as', User.logged_in_user.first_name)
            if User.logged_in_user.is_admin:
                return self.ADMIN_ACTIONS
            else:
                return self.USER_ACTIONS
        else:
            return self.LOGGED_OUT_ACTIONS

    @staticmethod
    def validate_input(user_input: int, actions: list):
        """
        Validate if the action number entered by user is valid
        :param user_input: Action number input by a user
        :param actions: List of available action
        :return: Action chosen
        """
        for action in actions:
            if user_input == action['value']:
                return action
        raise ValueError

    def user_interaction(self):
        """
        Display list of available actions and perform action based on user input
        """
        actions: list = self.get_actions()
        for action in actions:
            Log.log(action['message'], color='white')
        try:
            user_input: int = int(input())
            action: dict = self.validate_input(user_input, actions)
        except ValueError:
            Log.log('Incorrect Input', color='red')
            self.user_interaction()
            return
        action['action']()
        self.user_interaction()
