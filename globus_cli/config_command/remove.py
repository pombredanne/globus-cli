import click

from globus_cli.safeio import safeprint
from globus_cli.helpers import common_options
from globus_cli.config_command.helpers import load_config


@click.command('remove', help='Remove a value from the Globus Config')
@common_options(no_format_option=True)
@click.argument('parameter', required=True)
def remove_command(parameter):
    """
    Executor for `globus config remove`
    """
    conf = load_config()

    section = 'general'
    if '.' in parameter:
        section, parameter = parameter.split('.', 1)

    # ensure that the section exists
    if section not in conf:
        conf[section] = {}
    # remove the value for the given parameter
    del conf[section][parameter]

    # write to disk
    safeprint('Writing updated config to {}'.format(conf.filename))
    conf.write()
