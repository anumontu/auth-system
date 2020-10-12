import six
from PyInquirer import Token, style_from_dict

from pyfiglet import figlet_format
from termcolor import colored

input_style = style_from_dict({
    Token.QuestionMark: '#fac731 bold',
    Token.Answer: '#4688f1 bold',
    Token.Instruction: '',
    Token.Separator: '#cc5454',
    Token.Selected: '#0abf5b',
    Token.Pointer: '#673ab7 bold',
    Token.Question: '',
})


class Log:
    """
    Utility for logging to command line
    """

    @classmethod
    def log(cls, message: str, color: str, font: str = "slant", figlet: bool = False):
        """
        Method to display a message on command line
        :param message: Message to be displayed
        :param color: Color in which the message should be displayed
        :param font: Font in which the message should be displayed
        :param figlet: boolean to define if the message should be displayed as a banner
        """
        if colored:
            if not figlet:
                six.print_(colored(message, color))
            else:
                six.print_(colored(figlet_format(
                    message, font=font), color))
        else:
            six.print_(message)
