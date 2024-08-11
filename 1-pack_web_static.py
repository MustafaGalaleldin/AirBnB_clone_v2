#!/usr/bin/python3
"""
    a Fabric script that generates a .tgz archive from the contents of the
    web_static folder of AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local

env.hosts = ["52.201.220.63", "54.236.24.172"]
env.user = "ubuntu"


def do_restore():
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