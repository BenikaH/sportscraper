from sqlalchemy import *
import click


def initdb_statcast(db_username, db_password, db_hostname, db_name, db_tablename):
    db_password = ":" + db_password
    statcast_engine = create_engine("mysql+mysqldb://" + db_username + db_password + "@" + db_hostname + "/" + db_name)
    meta = MetaData(bind=statcast_engine)

    table_statcast = Table(db_tablename, meta,
        Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
        Column("index", Integer, nullable=True),
        Column("sz_bot", Float, nullable=True),
        Column("inning", Float, nullable=True),
        Column("pitch_number", Float, nullable=True),
        Column("hit_distance_sc", Float, nullable=True),
        Column("plate_z", Float, nullable=True),
        Column("plate_x", Float, nullable=True),
        Column("umpire", Float, nullable=True),
        Column("pitch_type", String(512), nullable=True),
        Column("spin_rate_deprecated", Float, nullable=True),
        Column("pos8_person_id", Float, nullable=True),
        Column("pos6_person_id", Float, nullable=True),
        Column("pos2_person_id.1", Float, nullable=True),
        Column("on_3b", Float, nullable=True),
        Column("release_pos_y", Float, nullable=True),
        Column("pos2_person_id", Float, nullable=True),
        Column("launch_speed", Float, nullable=True),
        Column("ay", Float, nullable=True),
        Column("ax", Float, nullable=True),
        Column("az", Float, nullable=True),
        Column("p_throws", String(512), nullable=True),
        Column("release_speed", Float, nullable=True),
        Column("break_length_deprecated", Float, nullable=True),
        Column("at_bat_number", Float, nullable=True),
        Column("vy0", Float, nullable=True),
        Column("away_team", String(512), nullable=True),
        Column("player_name", String(512), nullable=True),
        Column("zone", Float, nullable=True),
        Column("pos7_person_id", Float, nullable=True),
        Column("babip_value", Float, nullable=True),
        Column("bb_type", String(512), nullable=True),
        Column("release_spin_rate", Float, nullable=True),
        Column("effective_speed", Float, nullable=True),
        Column("pos3_person_id", Float, nullable=True),
        Column("hc_y", Float, nullable=True),
        Column("inning_topbot", String(512), nullable=True),
        Column("release_extension", Float, nullable=True),
        Column("on_1b", Float, nullable=True),
        Column("pos1_person_id", Float, nullable=True),
        Column("hit_location", Float, nullable=True),
        Column("release_pos_x", Float, nullable=True),
        Column("events", String(512), nullable=True),
        Column("release_pos_z", Float, nullable=True),
        Column("game_year", Float, nullable=True),
        Column("pos4_person_id", Float, nullable=True),
        Column("woba_value", Float, nullable=True),
        Column("description", String(512), nullable=True),
        Column("pfx_z", Float, nullable=True),
        Column("launch_angle", Float, nullable=True),
        Column("pitcher", Float, nullable=True),
        Column("strikes", Float, nullable=True),
        Column("pos9_person_id", Float, nullable=True),
        Column("batter", Float, nullable=True),
        Column("pfx_x", Float, nullable=True),
        Column("hc_x", Float, nullable=True),
        Column("on_2b", Float, nullable=True),
        Column("game_pk", Float, nullable=True),
        Column("spin_dir", Float, nullable=True),
        Column("iso_value", Float, nullable=True),
        Column("woba_denom", Float, nullable=True),
        Column("home_team", String(512), nullable=True),
        Column("balls", Float, nullable=True),
        Column("estimated_ba_using_speedangle", Float, nullable=True),
        Column("estimated_woba_using_speedangle", Float, nullable=True),
        Column("type", String(512), nullable=True),
        Column("tfs_deprecated", Float, nullable=True),
        Column("des", String(512), nullable=True),
        Column("game_type", String(512), nullable=True),
        Column("outs_when_up", Float, nullable=True),
        Column("vx0", Float, nullable=True),
        Column("sz_top", Float, nullable=True),
        Column("launch_speed_angle", Float, nullable=True),
        Column("stand", String(512), nullable=True),
        Column("game_date", DateTime, nullable=True),
        Column("break_angle_deprecated", Float, nullable=True),
        Column("vz0", Float, nullable=True),
        Column("sv_id", String(512), nullable=True),
        Column("tfs_zulu_deprecated", Float, nullable=True),
        Column("pos5_person_id", Float, nullable=True), extend_existing=True)

    meta.create_all(statcast_engine)

    return statcast_engine


def initdb_brooks(db_username, db_password, db_hostname, db_name, db_tablename):
    db_password = ":" + db_password
    brooks_engine = create_engine("mysql+mysqldb://" + db_username + db_password + "@" + db_hostname + "/" + db_name)
    meta = MetaData(bind=brooks_engine)

    table_brooks = Table(db_tablename, meta,
        Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
        Column("inning", Integer, nullable=True),
        Column("y0", Integer, nullable=True),
        Column("pitcher_team", String(512), nullable=True),
        Column("start_speed", Float, nullable=True),
        Column("play_guid", String(512), nullable=True),
        Column("pfx_zdatafile", Float, nullable=True),
        Column("z0", Float, nullable=True),
        Column("ab_id", Integer, nullable=True),
        Column("pitcher_id", Integer, nullable=True),
        Column("ay", Float, nullable=True),
        Column("zone_location", Float, nullable=True),
        Column("pxold", Float, nullable=True),
        Column("batter_id", Integer, nullable=True),
        Column("p_throws", String(512), nullable=True),
        Column("park_sv_id", String(512), nullable=True),
        Column("vy0", Float, nullable=True),
        Column("az", Float, nullable=True),
        Column("ab_count", Integer, nullable=True),
        Column("pz", Float, nullable=True),
        Column("spin", Float, nullable=True),
        Column("px", Float, nullable=True),
        Column("pfx_xdatafile", Float, nullable=True),
        Column("date_stamp", String(512), nullable=True),
        Column("gid", String(512), nullable=True),
        Column("ftime", Float, nullable=True),
        Column("tstart", Float, nullable=True),
        Column("uncorrected_pfx_x", Float, nullable=True),
        Column("uncorrected_pfx_z", Float, nullable=True),
        Column("type", String(512), nullable=True),
        Column("sz_bot", Float, nullable=True),
        Column("norm_ht", Float, nullable=True),
        Column("pfx_z", Float, nullable=True),
        Column("strikes", Integer, nullable=True),
        Column("mlbam_pitch_name", String(512), nullable=True),
        Column("pitch_con", Float, nullable=True),
        Column("pfx_x", Float, nullable=True),
        Column("vystart", Float, nullable=True),
        Column("ab_total", Integer, nullable=True),
        Column("pdes", String(512), nullable=True),
        Column("balls", Integer, nullable=True),
        Column("des", String(512), nullable=True),
        Column("x0", Float, nullable=True),
        Column("ax", Float, nullable=True),
        Column("sz_top", Float, nullable=True),
        Column("stand", String(512), nullable=True),
        Column("sb", Integer, nullable=True),
        Column("vz0", Float, nullable=True),
        Column("pzold", Float, nullable=True),
        Column("vx0", Float, nullable=True))

    meta.create_all(brooks_engine)

    return brooks_engine


def upload_block(data, db_engine, db_tablename):
    # try:
    data.to_sql(db_tablename, con=db_engine, if_exists='append', index=False, chunksize=10000)

    # except Exception as exc:
    #     click.echo('There was an error while trying to send to database...')
    #     click.echo(exc)
