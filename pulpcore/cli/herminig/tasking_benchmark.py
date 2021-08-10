import gettext
from typing import Any

import click
from pulpcore.cli.common.context import PluginRequirement, PulpContext, pass_pulp_context

_ = gettext.gettext


@click.command()
@click.option("--count", "-c", type=int)
@click.option("--sleep-secs", "-s", type=float)
@click.option("--truncate-tasks", is_flag=True)
@click.option("--failure-probability", "-p", type=float)
@click.option("--resources-n", "-N", type=int)
@click.option("--resources-k", "-K", type=int)
@pass_pulp_context
def tasking_benchmark(pulp_ctx: PulpContext, **kwargs: Any) -> None:
    """
    Trigger a burst of tasks in the tasking_system.
    """
    pulp_ctx.needs_plugin(PluginRequirement("herminig"))
    result = pulp_ctx.call(
        "herminig_tasking_benchmark_post", body={k: v for k, v in kwargs.items() if v is not None}
    )
    pulp_ctx.output_result(result)
