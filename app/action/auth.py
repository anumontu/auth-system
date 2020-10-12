from PyInquirer import prompt

from app.models.user import User
from app.util.common import input_style, Log
from app.util.validator import EmailValidator, EmptyValidator


class Auth:
    """
    Auth Actions for login and logout
    """

    @staticmethod
    def login():
        """
        Logs in the user using email and password
        """
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
        """
        Logs out the current user
        """
        User.logged_in_user = None
        Log.log('Logged out successfully', color='green')
