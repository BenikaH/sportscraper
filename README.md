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

To upload statcast to a database, try the following.  Be sure to substitute your database information where needed:
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

#### Pitching

To upload statcast to a database, try the following.  Be sure to substitute your database information where needed:
```bash
sportscraper pitching_upload \
    --start_date 2017-04-21 \
    --end_date 2017-04-28 \
    --db_username root \
    --db_password root \
    --db_hostname 127.0.0.1 \
    --db_name baseball \
    --db_tablename pitching
```

#### Batting

To upload statcast to a database, try the following.  Be sure to substitute your database information where needed:
```bash
sportscraper batting_upload \
    --start_date 2017-04-21 \
    --end_date 2017-04-28 \
    --db_username root \
    --db_password root \
    --db_hostname 127.0.0.1 \
    --db_name baseball \
    --db_tablename batting
```

#### Brooks Baseball PITCHf/x

To pull Brooks Baseball data into the database, you must first extract a csv file for the range you are looking for
from the Brooks Baseball Pitch Importer, located here:

> <https://github.com/mattdennewitz/baseball-brooks-pitch-importer>

Follow the instructions in the above repo to get a csv file.  Here's an example:

```bash
scrapy crawl pitches -a years=2014,2015 -t csv -o seasons-2014-2015.csv
```

Once you have the csv, just pass the path to the csv to sportscraper like so:

```bash
sportscraper brooks_upload \
    --path_to_csv spec-date.csv \
    --db_username root \
    --db_password root \
    --db_hostname 127.0.0.1 \
    --db_tablename 'brooks_small' \
    --db_name baseball
```