#!/usr/bin/python3
import fabric
from fabric.operations import local, run, put, sudo
from fabric.context_managers import cd
from datetime import datetime
from os import path


fabric.api.env.hosts = ["3.91.44.133", "35.227.49.226"]


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


def do_deploy(archive_path):
    """ distributes archive to web servers"""
    if not path.exists(archive_path):
        return False
    name = archive_path.split('/')[1]
    nne = name.split(".")[0]
    put(archive_path, "/tmp/{}".format(name))
    run("mkdir -p /data/web_static/releases/{}/".format(nne))
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(name, nne))
    run("rm /tmp/{}".format(name))
    what_to_mv = "/data/web_static/releases/{}/web_static/*".format(nne)
    where_to_mv = "/data/web_static/releases/{}/".format(nne)
    run("mv {} {}".format(what_to_mv, where_to_mv))
    run("rm -rf /data/web_static/releases/{}/web_static".format(nne))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
        .format(nne))
    return True
