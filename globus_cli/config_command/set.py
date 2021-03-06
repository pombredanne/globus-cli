import click

from globus_cli.safeio import safeprint
from globus_cli.helpers import common_options
from globus_cli.config_command.helpers import load_config


@click.command('set', help='Set a value in the Globus Config')
@common_options(no_format_option=True)
@click.argument('parameter', required=True)
@click.argument('value', required=True)
def set_command(value, parameter):
    """
    Executor for `globus config set`
    """
    conf = load_config()

    section = 'general'
    if '.' in parameter:
        section, parameter = parameter.split('.', 1)

    # ensure that the section exists
    if section not in conf:
        conf[section] = {}
    # set the value for the given parameter
    conf[section][parameter] = value

    # write to disk
    safeprint('Writing updated config to {}'.format(conf.filename))
    conf.write()
