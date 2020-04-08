#!/usr/bin/env bash
#setup the web servers
if [ ! -e "/usr/sbin/nginx" ]
then
        sudo apt-get -y update
        sudo apt-get -y upgrade
        sudo apt-get -y install nginx
        sudo service nginx start
fi
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "lela ya lela" | sudo tee /data/web_static/releases/test/index.html > /dev/null
if [ -e "/data/web_static/current" ]
then
    rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
new_str="\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}"
sudo sed -i " 25i $new_str" /etc/nginx/sites-enabled/default
sudo service nginx restart
