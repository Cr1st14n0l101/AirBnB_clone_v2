#!/usr/bin/python3
"""
Script that generates a .tgz
archive from the contents of
the web_static folder of your
AirBnB Clone repo
"""
from fabric.api import local
import datetime


def do_pack():
    """Compress the al files in folder webstatic"""
    now = datetime.datetime.now()
    path_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        now.year,
        now.month,
        now.day,
        now.hour,
        now.minute,
        now.second
        )
    local("mkdir -p versions")
    archiv = local("tar -cvzf {} web_static".format(path_file))
    if archiv.failed:
        return None
    return path_file
