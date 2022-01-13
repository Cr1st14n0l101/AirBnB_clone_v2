#!/usr/bin/python3
"""
Script that distributes an
archive to your web servers
with do_deploy function
"""
from fabric.api import *
import datetime
import os


env.hosts = ['34.139.172.28', '3.87.94.150']


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


def do_deploy(archive_path):
    """Deploy a file in ther nginx servers"""
    if not os.path.exists(archive_path):
        return False
    file = archive_path.split('/')[1]
    r = put('{}'.format(archive_path), '/tmp/')
    r = run("mkdir -p /data/web_static/releases/{}/".format(file[:-4]))
    if r.failed:
        return False
    r = run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
        file, file[:-4])
        )
    if r.failed:
        return False
    r = run("rm /tmp/{}".format(file))
    if r.failed:
        return False
    r = run("mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/".format(file[:-4], file[:-4]))
    if r.failed:
        return False
    r = run("rm -rf /data/web_static/releases/{}/web_static".format(file[:-4]))
    if r.failed:
        return False
    r = run("rm -rf /data/web_static/current")
    if r.failed:
        return False
    r = run(
        "ln -s /data/web_static/releases/{}/ /data/web_static/current".format(
            file[:-4])
            )
    if r.failed:
        return False
    return True


def deploy():
    """Creates and distributes an archive to the web servers"""
    r = do_pack()
    if not os.path.exists(r):
        return False
    r = do_deploy(r)
    return r
