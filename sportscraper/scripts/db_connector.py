from sqlalchemy import *
import click


def initdb_statcast(username, password, hostname, database, tablename):
    password = ":" + password
    statcast_engine = create_engine("mysql+mysqldb://" + username + password + "@" + hostname + "/" + database)
    meta = MetaData(bind=statcast_engine)

    table_statcast = Table(tablename, meta,
        Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
        Column("index", Integer, nullable=True),
        Column("sz_bot", Integer, nullable=True),
        Column("inning", Integer, nullable=True),
        Column("pitch_number", Integer, nullable=True),
        Column("hit_distance_sc", Integer, nullable=True),
        Column("plate_z", Integer, nullable=True),
        Column("plate_x", Integer, nullable=True),
        Column("umpire", Integer, nullable=True),
        Column("pitch_type", String(512), nullable=True),
        Column("spin_rate_deprecated", Integer, nullable=True),
        Column("pos8_person_id", Integer, nullable=True),
        Column("pos6_person_id", Integer, nullable=True),
        Column("pos2_person_id.1", Integer, nullable=True),
        Column("on_3b", Integer, nullable=True),
        Column("release_pos_y", Integer, nullable=True),
        Column("pos2_person_id", Integer, nullable=True),
        Column("launch_speed", Integer, nullable=True),
        Column("ay", Integer, nullable=True),
        Column("ax", Integer, nullable=True),
        Column("az", Integer, nullable=True),
        Column("p_throws", String(512), nullable=True),
        Column("release_speed", Integer, nullable=True),
        Column("break_length_deprecated", Integer, nullable=True),
        Column("at_bat_number", Integer, nullable=True),
        Column("vy0", Integer, nullable=True),
        Column("away_team", String(512), nullable=True),
        Column("player_name", String(512), nullable=True),
        Column("zone", Integer, nullable=True),
        Column("pos7_person_id", Integer, nullable=True),
        Column("babip_value", Integer, nullable=True),
        Column("bb_type", String(512), nullable=True),
        Column("release_spin_rate", Integer, nullable=True),
        Column("effective_speed", Integer, nullable=True),
        Column("pos3_person_id", Integer, nullable=True),
        Column("hc_y", Integer, nullable=True),
        Column("inning_topbot", String(512), nullable=True),
        Column("release_extension", Integer, nullable=True),
        Column("on_1b", Integer, nullable=True),
        Column("pos1_person_id", Integer, nullable=True),
        Column("hit_location", Integer, nullable=True),
        Column("release_pos_x", Integer, nullable=True),
        Column("events", String(512), nullable=True),
        Column("release_pos_z", Integer, nullable=True),
        Column("game_year", Integer, nullable=True),
        Column("pos4_person_id", Integer, nullable=True),
        Column("woba_value", Integer, nullable=True),
        Column("description", String(512), nullable=True),
        Column("pfx_z", Integer, nullable=True),
        Column("launch_angle", Integer, nullable=True),
        Column("pitcher", Integer, nullable=True),
        Column("strikes", Integer, nullable=True),
        Column("pos9_person_id", Integer, nullable=True),
        Column("batter", Integer, nullable=True),
        Column("pfx_x", Integer, nullable=True),
        Column("hc_x", Integer, nullable=True),
        Column("on_2b", Integer, nullable=True),
        Column("game_pk", Integer, nullable=True),
        Column("spin_dir", Integer, nullable=True),
        Column("iso_value", Integer, nullable=True),
        Column("woba_denom", Integer, nullable=True),
        Column("home_team", String(512), nullable=True),
        Column("balls", Integer, nullable=True),
        Column("estimated_ba_using_speedangle", Integer, nullable=True),
        Column("estimated_woba_using_speedangle", Integer, nullable=True),
        Column("type", String(512), nullable=True),
        Column("tfs_deprecated", Integer, nullable=True),
        Column("des", String(512), nullable=True),
        Column("game_type", String(512), nullable=True),
        Column("outs_when_up", Integer, nullable=True),
        Column("vx0", Integer, nullable=True),
        Column("sz_top", Integer, nullable=True),
        Column("launch_speed_angle", Integer, nullable=True),
        Column("stand", String(512), nullable=True),
        Column("game_date", DateTime, nullable=True),
        Column("break_angle_deprecated", Integer, nullable=True),
        Column("vz0", Integer, nullable=True),
        Column("sv_id", String(512), nullable=True),
        Column("tfs_zulu_deprecated", Integer, nullable=True),
        Column("pos5_person_id", Integer, nullable=True), extend_existing=True)

    meta.create_all(statcast_engine)

    return statcast_engine


def initdb_brooks(username, password, hostname, database):
    brooks_engine = create_engine("mysql+mysqldb://" + username + password + "@" + hostname + "/" + database)
    meta = MetaData(bind=engine)

    table_statcast = Table('statcast', meta,
        Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
        Column("index", Integer, nullable=True), extend_existing=True)

    meta.create_all(engine)

    return brooks_engine


def upload_block(data, statcast_engine, db_tablename):
    # try:
    data.to_sql(db_tablename, con=statcast_engine, if_exists='append', index=False)

    # except Exception as exc:
    #     click.echo('There was an error while trying to send to database...')
    #     click.echo(exc)
