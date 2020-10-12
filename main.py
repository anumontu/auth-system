import click

from app.interaction.interaction import Interaction
from app.util.common import Log
from app.util.setup import Setup


@click.command()
def main():
    """
    Simple CLI for auth systems
    """
    Log.log("AUTH SYSTEM", color="white", figlet=True)
    Log.log("Welcome to Auth System CLI", "green")
    Setup().init()
    Interaction().user_interaction()


if __name__ == '__main__':
    main()
