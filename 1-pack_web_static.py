#!/usr/bin/pyhton3
"""
    a Fabric script that generates a .tgz archive from the contents of the
    web_static folder of AirBnB Clone repo, using the function do_pack.
"""
from datetime import datetime
from fabric.api import local

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
