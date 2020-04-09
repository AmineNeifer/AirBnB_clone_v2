#!/usr/bin/python3
import fabric
from fabric.operations import local
from datetime import datetime


def do_pack():
    """ compress web_static files"""
    try:
        local("mkdir -p versions")
        x = str(datetime.now()).split(".")[0].replace(' ', '')
        x = x.replace('-', '').replace(':', '')
        path = "versions/web_static_{}".format(x)
        cmd = "tar -cvzf {}.tgz web_static".format(path)
        local(cmd)
        return path
    except:
        return None
