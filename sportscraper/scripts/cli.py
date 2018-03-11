import click

# local packages
from .pullbrooks import *


@click.group()
def cli():
    pass


@click.command()
def test():
    click.echo('test worked')


@click.command()
def pulldeps():
    cmd_pull_brooks()


# add block of commands
cli.add_command(test)
cli.add_command(pulldeps)

