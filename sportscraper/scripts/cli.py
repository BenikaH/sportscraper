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


# @click.command('--path_to_csv', '-c')
# def brooks_echo(path_to_csv):
#     cmd_brooks_echo(path_to_csv)


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
@click.option('--db_name', '-d')
@click.option('--db_tablename', '-t')
def statcast_upload(start_date, end_date, db_username, db_password, db_hostname, db_name, db_tablename):
    cmd_statcast_upload(start_date, end_date, db_username, db_password, db_hostname, db_name, db_tablename)


@click.command()
@click.option('--path_to_csv', '-c')
@click.option('--db_username', '-u')
@click.option('--db_password', '-p')
@click.option('--db_hostname', '-h')
@click.option('--db_name', '-d')
@click.option('--db_tablename', '-t')
def brooks_upload(path_to_csv, db_username, db_password, db_hostname, db_name, db_tablename):
    cmd_brooks_upload(path_to_csv, db_username, db_password, db_hostname, db_name, db_tablename)


# add block of commands
cli.add_command(test)
cli.add_command(statcast_echo)
cli.add_command(statcast_upload)
# cli.add_command(brooks_echo)
cli.add_command(brooks_upload)

