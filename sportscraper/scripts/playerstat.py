from pybaseball import statcast
from pybaseball import playerid_lookup
from pybaseball import statcast_batter
from pybaseball import statcast_pitcher
from pybaseball import pitching_stats
from pandas import Series
from sqlalchemy import create_engine, MetaData, TEXT, Integer, Table, Column, ForeignKey

# data = pitching_stats(2016, 2017)
#
# data.head()

# kershaw_stats = statcast_pitcher('2017-06-01', '2017-07-01')
# kershaw_stats.head()

# data = statcast(start_dt='2017-03-08', end_dt='2017-03-28')

# data.head()

# fh = open('output.html', 'w')
# fh.write(str(data.to_html()))
# fh.close
#
# fh = open('output.sql', 'w')
# fh.write(str(data.to_sql('stats', flavor='mysql', if_exists='append')))
# fh.close


def cmd_playerstat():

    data = statcast(start_dt='2017-03-08', end_dt='2017-04-28')

    # data

    count = 0
    for index, row, in data.iterrows():
        if count > 1:
            break
        # print(row)
        for index, value in row.iteritems():
            print('index=' + str(index))
            print('value=' + str(value))
        count = count + 1

    # engine = create_engine("mysql+mysqldb://root:" + 'NEW PASSWORD' + "@localhost/parrot_db")
    # meta = MetaData(bind=engine)
    #
    # fh = open('output.sql', 'w')
    # fh.write(str(data.to_sql('player_name', engine, flavor='mysql', if_exists='append')))
    # fh.close


