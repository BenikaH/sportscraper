import click

# local packages
from brooks import *
from statcast import *
from pitching import *
from batting import *
from teambatting import *
from teampitching import *


@click.group()
def cli():
    pass


@click.command()
@click.option('--hostname', '-h', default='nothing')
def test(hostname):
    click.echo('testing input hostname = ' + hostname)


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
@click.option('--start_year', '-s')
@click.option('--end_year', '-e')
@click.option('--db_username', '-u')
@click.option('--db_password', '-p')
@click.option('--db_hostname', '-h')
@click.option('--db_name', '-d')
@click.option('--db_tablename', '-t')
def pitching_upload(start_year, end_year, db_username, db_password, db_hostname, db_name, db_tablename):
    cmd_pitching_upload(start_year, end_year, db_username, db_password, db_hostname, db_name, db_tablename)


@click.command()
@click.option('--start_year', '-s')
@click.option('--end_year', '-e')
@click.option('--db_username', '-u')
@click.option('--db_password', '-p')
@click.option('--db_hostname', '-h')
@click.option('--db_name', '-d')
@click.option('--db_tablename', '-t')
def batting_upload(start_year, end_year, db_username, db_password, db_hostname, db_name, db_tablename):
    cmd_batting_upload(start_year, end_year, db_username, db_password, db_hostname, db_name, db_tablename)


@click.command()
@click.option('--start_year', '-s')
@click.option('--end_year', '-e')
@click.option('--db_username', '-u')
@click.option('--db_password', '-p')
@click.option('--db_hostname', '-h')
@click.option('--db_name', '-d')
@click.option('--db_tablename', '-t')
def teampitching_upload(start_year, end_year, db_username, db_password, db_hostname, db_name, db_tablename):
    cmd_teampitching_upload(start_year, end_year, db_username, db_password, db_hostname, db_name, db_tablename)


@click.command()
@click.option('--start_year', '-s')
@click.option('--end_year', '-e')
@click.option('--db_username', '-u')
@click.option('--db_password', '-p')
@click.option('--db_hostname', '-h')
@click.option('--db_name', '-d')
@click.option('--db_tablename', '-t')
def teambatting_upload(start_year, end_year, db_username, db_password, db_hostname, db_name, db_tablename):
    cmd_teambatting_upload(start_year, end_year, db_username, db_password, db_hostname, db_name, db_tablename)

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
cli.add_command(statcast_upload)
cli.add_command(brooks_upload)
cli.add_command(pitching_upload)
cli.add_command(batting_upload)
cli.add_command(teampitching_upload)
cli.add_command(teambatting_upload)

