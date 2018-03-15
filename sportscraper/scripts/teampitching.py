from pybaseball import team_pitching
from db_connector import *
import pandas as pd

import click


def cmd_teampitching_upload(start_year, end_year, db_username, db_password, db_hostname, db_name, db_tablename):

    click.echo('[[[ PULLING TEAMPITCHING DATAFRAME ]]]')

    engine = initdb_pitching(db_username, db_password, db_hostname, db_name, db_tablename)

    click.echo(str('Pulling data...'))
    try:
        data = team_pitching(start_year, end_year)
        data.columns = data.columns.str.replace('%', '')
        upload_block(data, engine, db_tablename)
    except Exception as exc:
        click.echo("ERROR pulling down data - Error was = " + str(exc))
    else:
        click.echo(str('SUCCESS, pulled ' + str(data.shape[0]) + ' records'))

