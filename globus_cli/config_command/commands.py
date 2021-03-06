import click
from globus_cli.helpers import common_options

from globus_cli.config_command.edit import edit_command
from globus_cli.config_command.init import init_command
from globus_cli.config_command.remove import remove_command
from globus_cli.config_command.set import set_command
from globus_cli.config_command.show import show_command


@click.group('config', short_help=(
    'Modify, view, and manage your Globus CLI config.'), help=("""\
    Modify, view, and manage your Globus CLI config.

    Many commands accept PARAMETERs, names which identify settings in the
    config file. If a PARAMETER includes any dots, the part prior to its first
    dot is used as the config section name, and the remainder is the name of
    an option in that section.

    The default section name is always "general", which is where most Globus
    Config values are kept.

    \b
    For example, you might use
        $ globus config show auth_token
    to display your current 'auth_token' from the 'general' section.
    You can equally well use
        $ globus config show general.auth_token
    to show the same value more explicitly.
    """))
@common_options
def config_command():
    pass


config_command.add_command(edit_command)
config_command.add_command(init_command)
config_command.add_command(remove_command)
config_command.add_command(set_command)
config_command.add_command(show_command)
