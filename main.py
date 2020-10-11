import click

from interaction.interaction import Interaction
from models.resource import Resource
from models.role import Role
from models.role_resource import RoleResource
from models.user import User
from models.user_role import UserRole
from util.common import Log
from util.setup import Setup


@click.command()
def main():
    """
    Simple CLI for auth systems
    """
    Log.log("AUTH SYSTEM", color="white", figlet=True)
    Log.log("Welcome to Auth System CLI", "green")
    Setup().init()
    # print(User.users)
    # print(Resource.resources)
    # print(Role.roles)
    # print(RoleResource.role_resources)
    # print(UserRole.user_roles)
    Interaction().user_interaction()


if __name__ == '__main__':
    main()
