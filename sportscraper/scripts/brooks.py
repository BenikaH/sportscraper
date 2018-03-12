import click

import git
import os


def cmd_pull_brooks():
    try:
        os.stat(os.getcwd() + '/.deps/baseball-brooks-pitch-importer/')
    except:
        if not os.listdir(os.getcwd()):
            try:
                os.stat(os.getcwd() + '/.deps/')
            except:
                os.mkdir(os.getcwd() + '/.deps/')
            click.echo("Pulling the brooks importer git repo...")
            try:
                git.Git(os.getcwd() + "/.deps/").clone("git://github.com/BenikaH/baseball-brooks-pitch-importer")
            except:
                click.echo("There was a problem pulling the brooks repo...")
        else:
            click.echo('Your current directory is not empty.  Please navigate to an empty directory to run this utility.')
    else:
        click.echo("Looks like the brooks repo is already cloned...")


# def cmd_brooks_echo(start_date, end_date):

    # data = statcast(start_dt=start_date, end_dt=end_date)

    # click.echo(data.to_string())