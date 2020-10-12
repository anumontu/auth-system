import re

from PyInquirer import Validator, ValidationError
from prompt_toolkit.document import Document


class EmailValidator(Validator):
    """
    Validate if input is a valid email
    """
    pattern: str = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"

    def validate(self, email: Document):
        if len(email.text):
            if re.match(self.pattern, email.text):
                return True
            else:
                raise ValidationError(
                    message="Invalid email",
                    cursor_position=len(email.text))
        else:
            raise ValidationError(
                message="You can't leave this blank",
                cursor_position=len(email.text))


class EmptyValidator(Validator):
    """
    Validate if input is not empty
    """

    def validate(self, value: Document):
        if len(value.text):
            return True
        else:
            raise ValidationError(
                message="You can't leave this blank",
                cursor_position=len(value.text))
