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
        archive_name = archive_path.split("/")[-1]
        arch = archive_name.split(".")[0]
        put(archive_path, "/tmp/")
        run(f"mkdir -p /data/web_static/releases/{arch}")
        run(f"tar -xzf /tmp/{archive_name} -C"
            f"/data/web_static/releases/{arch}")
        run(f"rm -f /tmp/{archive_name}")
        run("rm -rf /data/web_static/current 2> /dev/null")
        run(f"mv -f /data/web_static/releases/{arch}/web_static/* "
            f"/data/web_static/releases/{arch}")
        run("rm -rf /data/web_static/releases/{arch}/web_static")
        sudo(f"ln -sf /data/web_static/releases/{arch}/ "
             "/data/web_static/current")
        return True
    except Exception:
        return False
