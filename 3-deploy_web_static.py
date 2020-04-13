#!/usr/bin/python3
"""
Full deployment of web files
"""
import fabric
from fabric.api import local, put, env, run
from datetime import datetime


env.hosts = ["3.91.44.133", "35.227.49.226"]


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
    """
    Distributes an archive to your web servers.
    """
    name = archive_path.split('/')[1]
    nne = name.split(".")[0]
    rel = "/data/web_static/releases"
    cur = "/data/web_static/current"
    if not put(archive_path, "/tmp/").succeeded:
        return False
    if not run("mkdir -p {}/{}/".format(rel, nne)).succeeded:
        return False
    if not run("tar -xzf /tmp/{} -C {}/{}/".format(name, rel, nne)).succeeded:
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


def deploy():
    """
    combining both do_pack and do_deploy
    basically, full deployment
    """
    path = do_pack()
    if path is None:
        return False
    arch_path = "{}.tgz".format(path)
    return do_deploy(arch_path)
