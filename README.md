# Sportscraper
###### A tool for gathering information from MLB statcast and Brooks Baseball's PITCHf/x tool and importing the dataframes to a mysql database.

#### Requirements
Requires the following packages:
* click
* pybaseball
* gitpython
* sqlalchemy
* pandas

#### Installation

This could one day be added to PyPi, but for now just do the following to install:

For an actively editable dev state (doesn't require reinstall after script changes):
```bash
pip install -e .[test]
```

For a system level installation. Ensure you are in the root directory (same as this readme), then run:
```bash
pip install
```

### Usage

#### Statcast

To pull statcast data and echo to shell:
```bash
sportscraper statcast_echo --start_date 2017-04-22 --end_date 2017-04-25
```

To upload to a database, try the following.  Be sure to substitute your database information where needed:
```bash
sportscraper statcast_upload \
    --start_date 2017-04-21 \
    --end_date 2017-04-28 \
    --db_username root \
    --db_password root \
    --db_hostname 127.0.0.1 \
    --db_name baseball \
    --db_tablename statcast
```

The tool is designed to run one query per day in the range specified so that it doesn't hit the 30k row limit per query for MLB's statcast tool.

#### Brooks Baseball PITCHf/x

Coming soon...