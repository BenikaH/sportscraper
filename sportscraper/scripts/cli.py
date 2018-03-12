import click

# local packages
from .brooks import *
from .statcast import *
from db_connector import *


@click.group()
def cli():
    pass


@click.command()
@click.option('--hostname', '-h', default='nothing')
def test(hostname):
    click.echo('testing input hostname = ' + hostname)


@click.command()
def pulldeps():
    cmd_pull_brooks()


@click.command()
@click.option('--start_date', '-s')
@click.option('--end_date', '-e')
def statcast_echo(start_date, end_date):
    cmd_statcast_echo(start_date, end_date)


@click.command()
@click.option('--start_date', '-s')
@click.option('--end_date', '-e')
@click.option('--db_username', '-u')
@click.option('--db_password', '-p')
@click.option('--db_hostname', '-h')
@click.option('--db_database', '-d')
@click.option('--db_tablename', '-t')
def statcast_upload(start_date, end_date, db_username, db_password, db_hostname, db_database, db_tablename):
    cmd_statcast_upload(start_date, end_date, db_username, db_password, db_hostname, db_database, db_tablename)


# add block of commands
cli.add_command(test)
cli.add_command(pulldeps)
cli.add_command(statcast_echo)
cli.add_command(statcast_upload)

