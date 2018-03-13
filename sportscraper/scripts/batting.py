from pybaseball import statcast, pitching_stats
from db_connector import *
import pandas as pd

import click


def cmd_batting_upload(start_date, end_date, db_username, db_password, db_hostname, db_name, db_tablename):

    click.echo('[[[ PULLING BATTING DATAFRAME ]]]')

    engine = initdb_pitching(db_username, db_password, db_hostname, db_name, db_tablename)

    click.echo(str('Pulling data...'))
    try:
        data = pitching_stats(start_date, end_date)
        data.columns = data.columns.str.replace('%', '')
        upload_block(data, engine, db_tablename)
    except Exception as exc:
        click.echo("ERROR pulling down data - Error was = " + str(exc))
    else:
        click.echo(str('SUCCESS, pulled ' + str(data.shape[0]) + ' records'))

