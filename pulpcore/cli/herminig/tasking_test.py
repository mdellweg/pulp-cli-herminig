import typing as t

import click
from pulp_glue.common.context import PluginRequirement
from pulpcore.cli.common.generic import PulpCLIContext, pass_pulp_context


@click.command()
@click.option("--count", "-c", type=int)
@click.option("--sleep-secs", "-s", type=float)
@pass_pulp_context
def tasking_test(pulp_ctx: PulpCLIContext, **kwargs: t.Any) -> None:
    """
    Trigger a burst of tasks in the tasking_system.
    """
    pulp_ctx.needs_plugin(PluginRequirement("herminig"))
    result = pulp_ctx.call(
        "herminig_tasking_test_post", body={k: v for k, v in kwargs.items() if v is not None}
    )
    pulp_ctx.output_result(result)
