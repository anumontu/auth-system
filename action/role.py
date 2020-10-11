from PyInquirer import prompt

from models.user import User
from models.user_role import UserRole
from util.common import Log, input_style


class RoleActions:

    @staticmethod
    def check_resource_access():
        roles = UserRole.get_roles(User.logged_in_user)
        if not roles:
            Log.log('No roles associated', color='red')
            return
        for role in UserRole.get_roles(User.logged_in_user):
            Log.log(role.name, color='green')

    @staticmethod
    def add_role(user: User):
        roles: list = UserRole.get_other_roles(user)
        if not roles:
            Log.log('No more roles available', color='red')
            return
        add_role_questions: list = [
            {
                'type': 'list',
                'name': 'role_name',
                'message': 'Choose Role',
                'choices': [role.name for role in roles]
            }
        ]
        answers: dict = prompt(add_role_questions, style=input_style)
        for role in roles:
            if role.name == answers['role_name']:
                UserRole.create(user, role)
                Log.log('Role assigned successfully', color='green')
                break

    @staticmethod
    def remove_role(user: User):
        user_roles: list = UserRole.get_user_roles(user)
        if not user_roles:
            Log.log('No roles assigned', color='red')
            return
        remove_role_questions: list = [
            {
                'type': 'list',
                'name': 'role_name',
                'message': 'Choose Role',
                'choices': [user_role.role.name for user_role in user_roles]
            }
        ]
        answers: dict = prompt(remove_role_questions, style=input_style)
        for index, user_role in enumerate(UserRole.user_roles):
            if user_role.user.id == user.id and user_role.role.name == answers['role_name']:
                UserRole.user_roles.pop(index)
                Log.log('Role unassigned successfully', color='green')
                break

    @staticmethod
    def edit_role():
        users: list = [user.email for user in User.get_users(is_admin=False)]
        if not users:
            Log.log('Users not found', color='red')
            return
        edit_role_questions: list = [
            {
                'type': 'list',
                'name': 'email',
                'message': 'Choose User',
                'choices': users
            },
            {
                'type': 'list',
                'name': 'add_remove_role',
                'message': 'Add or Remove Role',
                'choices': ['Add', 'Remove'],
                'filter': lambda val: val.lower()
            }
        ]
        answers: dict = prompt(edit_role_questions, style=input_style)
        user: User = User.get_user(answers['email'])
        if answers['add_remove_role'] == 'add':
            RoleActions.add_role(user)
        else:
            RoleActions.remove_role(user)
