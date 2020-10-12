from PyInquirer import prompt

from app.models.user import User
from app.util.common import input_style, Log
from app.util.validator import EmailValidator, EmptyValidator


class UserActions:

    @staticmethod
    def create_user():
        """
        Admin action to create a user
        """
        create_user_questions: list = [
            {
                'type': 'input',
                'name': 'first_name',
                'message': 'First Name',
                'validate': EmptyValidator
            },
            {
                'type': 'input',
                'name': 'last_name',
                'message': 'Last Name',
                'validate': EmptyValidator
            },
            {
                'type': 'input',
                'name': 'email',
                'message': 'Email',
                'validate': EmailValidator
            },
            {
                'type': 'password',
                'name': 'password',
                'message': 'Password',
                'validate': EmptyValidator
            },
            {
                'type': 'list',
                'name': 'is_admin',
                'message': 'Is Admin User',
                'choices': ['Yes', 'No'],
                'filter': lambda val: val.lower() == 'yes'
            },
        ]
        answers: dict = prompt(create_user_questions, style=input_style)
        user: User = User.get_user(answers['email'])
        if user:
            Log.log('User already exists with this email', color='red')
            return
        User.create(
            answers['first_name'], answers['last_name'], answers['email'], answers['password'],
            is_admin=answers['is_admin']
        )
        Log.log('User created successfully', color='green')
