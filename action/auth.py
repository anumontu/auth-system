from models.user import User
from util.common import input_style, Log
from util.validator import EmailValidator, EmptyValidator
from PyInquirer import prompt


class Auth:

    @staticmethod
    def login():
        User.logged_in_user = None
        login_questions: list = [
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
            }
        ]
        answers: dict = prompt(login_questions, style=input_style)
        for user in User.users:
            if user.email == answers['email'] and user.verify_password(answers['password']):
                User.logged_in_user = user
                Log.log('Logged in successfully', color='green')
                return user
        Log.log('Invalid login credentials', color='red')

    @staticmethod
    def logout():
        User.logged_in_user = None
        Log.log('Logged out successfully', color='green')
