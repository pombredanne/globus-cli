"""
This module defines all of the tools needed to decorate the top-level `globus`
command. All customizations that apply specifically to this main command go
here.
Ultimately, `globus_cli.parsing` will export only the decorator defined here,
and all other components will be hidden internals.
"""

import sys
import click

from globus_cli.parsing.excepthook import custom_except_hook
from globus_cli.helpers import common_options


# there is a single global object for all click contexts, a shared dict
_global_click_obj = {}


class TopLevelGroup(click.Group):
    """
    This is a custom command type which is basically a click.Group, but is
    designed specifically for the top level command.
    It's specialization is that it catches all exceptions from subcommands and
    passes them to a custom error handler.
    """
    def invoke(self, ctx):
        try:
            return super(TopLevelGroup, self).invoke(ctx)
        except Exception:
            custom_except_hook(sys.exc_info())


def globus_main_func(f):
    f = click.group('globus', context_settings=dict(obj=_global_click_obj),
                    cls=TopLevelGroup)(f)
    f = common_options(f)
    return f
