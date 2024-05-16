import typing as t

import click
from pulpcore.cli.common.generic import pulp_group
from pulpcore.cli.common.debug import debug

from pulpcore.cli.herminig.tasking_benchmark import tasking_benchmark
from pulpcore.cli.herminig.tasking_test import tasking_test

__version__ = "0.0.1.dev0"


@pulp_group(name="herminig")
def herminig_group() -> None:
    pass


def mount(main: click.Group, **kwargs: t.Any) -> None:
    herminig_group.add_command(tasking_benchmark)
    herminig_group.add_command(tasking_test)
    main.add_command(herminig_group)
