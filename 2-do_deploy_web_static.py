#!/usr/bin/python3
"""
    a Fabric script that distributes an archive to your web servers
    using the function do_deploy
"""
from fabric.api import run, env, put, sudo
from os.path import exists

env.hosts = ["52.201.220.63", "54.236.24.172"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """The fabric function for the process"""
    if not archive_path or exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception:
        return False
