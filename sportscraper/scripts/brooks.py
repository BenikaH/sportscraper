import click
from pandas import *
from .db_connector import *


def brooks_csv_to_dataframe(path_to_csv):
    brooks_dataframe = read_csv(path_to_csv)
    return brooks_dataframe


def cmd_brooks_echo(path_to_csv):
    brooks_dataframe = brooks_csv_to_dataframe(path_to_csv)
    click.echo(brooks_dataframe.head())


def cmd_brooks_upload(path_to_csv, db_username, db_password, db_hostname, db_name, db_tablename):

    click.echo('[[[ PULLING BROOKS CSV INTO DATAFRAME ]]]')

    brooks_engine = initdb_brooks(db_username, db_password, db_hostname, db_name, db_tablename)

    click.echo("Grabbing brooks data from csv located at = " + str(path_to_csv))

    brooks_data = brooks_csv_to_dataframe(path_to_csv)
    brooks_data = brooks_data.drop(columns=['id'])

    click.echo("Inserting into database...")

    upload_block(brooks_data, brooks_engine, db_tablename)

