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
    fname = archive_path.split('/')[-1]
    r = put(archive_path, "/tmp/")
    if r.failed:
        return False
    path = '/data/web_static/releases/' + fname[:-4]
    r = run('mkdir -p %s' % path)
    if r.failed:
        return False
    r = run('tar -xzf /tmp/%s -C /data/web_static/releases/%s/' %
            (fname, fname[:-4]))
    if r.failed:
        return False
    r = run('rm /tmp/%s' % fname)
    if r.failed:
        return False
    r = run('mv /data/web_static/releases/%s/web_static/*\
    /data/web_static/releases/%s' % (fname[:-4], fname[:-4]))
    if r.failed:
        return False
    r = run('rm -rf /data/web_static/releases/%s/web_static' % fname[:-4])
    if r.failed:
        return False
    r = run('rm -rf /data/web_static/current')
    if r.failed:
        return False
    r = run('ln -s /data/web_static/releases/%s /data/web_static/current'
            % fname[:-4])
    if r.failed:
        return False
    return True
