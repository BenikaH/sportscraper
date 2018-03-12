from pybaseball import statcast
from db_connector import *
import pandas as pd

import click


def cmd_statcast_upload(start_date, end_date, db_username, db_password, db_hostname, db_database, db_tablename):

    click.echo('[[[ PULLING STATCAST DATAFRAME ]]]')

    statcast_engine = initdb_statcast(db_username, db_password, db_hostname, db_database, db_tablename)

    click.echo("Breaking up into queries by day to avoid the 30k row cap...")

    for day in pd.date_range(start_date, end_date):
        click.echo(str(day.date()) + ' - Pulling data...')
        try:
            data = statcast(start_dt=str(day.date()), end_dt=str(day.date()))
            upload_block(data, statcast_engine, db_tablename)
        except Exception as exc:
            click.echo(str(day.date()) + " - ERROR pulling down data - Error was = " + str(exc))
        else:
            click.echo(str(day.date()) + ' - SUCCESS, pulled ' + str(data.shape[0]) + ' records')




def cmd_statcast_echo(start_date, end_date):

    dates = pd.date_range(start_date, end_date).tolist()

    data = statcast(start_dt=start_date, end_dt=end_date)

    click.echo(data.head())

