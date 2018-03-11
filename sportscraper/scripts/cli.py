import click

# local packages
from .pullbrooks import *
from .playerstat import *


@click.group()
def cli():
    pass


@click.command()
def test():
    click.echo('test worked')


@click.command()
def pulldeps():
    cmd_pull_brooks()


@click.command()
def playerstat():
    cmd_playerstat()


# add block of commands
cli.add_command(test)
cli.add_command(pulldeps)
cli.add_command(playerstat)

