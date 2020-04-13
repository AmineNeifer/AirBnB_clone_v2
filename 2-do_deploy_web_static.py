#!/usr/bin/python3
"""
generates a .tgz archive from webstatic
and distributes it to the web servers
"""
import fabric
from fabric.operations import local, run, put, env
from datetime import datetime


env.hosts = ["3.91.44.133", "35.227.49.226"]
env.user = ["ubuntu"]
api.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """
    distributes archive to web servers
    """
    name = archive_path.split('/')[1]
    nne = name.split(".")[0]
    rel = "/data/web_static/releases"
    cur = "/data/web_static/current"
    if not put(archive_path, "/tmp/{}".format(name)).succeeded:
        return False
    if not run("mkdir -p {}/{}/".format(rel, nne)).succeeded:
        return False
    if not run("tar -xzf /tmp/{} -C {}/{}/".format(rel, name, nne)).succeeded:
        return False
    if not run("rm /tmp/{}".format(name)).succeeded:
        return False
    what_to_mv = "{}/{}/web_static/*".format(rel, nne)
    where_to_mv = "{}/{}/".format(rel, nne)
    if not run("mv {} {}".format(what_to_mv, where_to_mv)).succeeded:
        return False
    if not run("rm -rf {}/{}/web_static".format(rel, nne)).succeeded:
        return False
    if not run("rm -rf /data/web_static/current").succeeded:
        return False
    if not run("ln -s {}/{}/ {}".format(rel, nne, cur)).succeeded:
        return False
    return True
