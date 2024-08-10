#!/usr/bin/python3
"""
   a Fabric script that creates and distributes an archive to your web servers
   using the function deploy
"""
from fabric.api import local
from datetime import datetime
from os.path import exists

env.hosts = ["52.201.220.63", "54.236.24.172"]
env.user = "ubuntu"


def do_pack():
    """
        return the archive path if the archive has been correctly generated.
        Otherwise, it should return None
    """
    time = datetime.now()
    time_str = time.strftime("%Y%m%d%H%M%S")
    filename = f"web_static_{time_str}.tgz"
    local("mkdir -p versions")
    stat = local(f"tar czvf versions/{filename} web_static")
    if stat:
        return f"versions/{filename}"
    else:
        return None


def do_deploy(archive_path):
    """
    a Fabric script that distributes an archive to your web servers
    using the function do_deploy
    """
    if exists(archive_path) is False:
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


def deploy():
    """
    the main function for deploying, it is a Fabric function
    that creates and distributes an archive to your web servers
    """
    arch_path = do_pack()
    if arch_path is None:
        return False
    return do_deploy(arch_path)
