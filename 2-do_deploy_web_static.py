#!/usr/bin/python3
"""
    a Fabric script that distributes an archive to your web servers
    using the function do_deploy
"""
from fabric.api import run, env, put
from os.path import exists

env.hosts = ["52.201.220.63", "54.236.24.172"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """The fabric function for the process"""
    if not archive_path or exists(archive_path) is False:
        return False
    try:
        archive_name = archive_path[9:len(archive_path) - 4]
        put(archive_path, "/tmp/")
        run(f"sudo mkdir -p /data/web_static/releases/{archive_name}")
        run(f"sudo tar xzf /tmp/{archive_path[9:]} -C"
            f"/data/web_static/releases/{archive_name}")
        run(f"sudo rm -f /tmp/{archive_path[9:]}")
        run("sudo rm -rf /data/web_static/current 2> /dev/null")
        run(f"sudo mv /data/web_static/releases/{archive_name}/web_static/* "
            f"/data/web_static/releases/{archive_name}")
        run("sudo rm -rf /data/web_static/releases/{archive_name}/web_static")
        run(f"sudo ln -sf /data/web_static/releases/{archive_name}/ "
            "/data/web_static/current")
        return True
    except Exception:
        return False
