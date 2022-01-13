#!/usr/bin/env bash                                                                                                                                                               
# Sets up your web servers for                                                                                                                                                    
# the deployment of web_static.                                                                                                                                                   
apt update
apt-get -y install nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
BODY="<html>                                                                                                                                                                      
  <head>                                                                                                                                                                          
  </head>                                                                                                                                                                         
  <body>                                                                                                                                                                          
    Holberton School                                                                                                                                                              
  </body>                                                                                                                                                                         
</html>"
echo "$BODY" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current 
chown -R ubuntu /data/
chgrp -R ubuntu /data/
sed -i '/listen 80 default_server/a location /hbnb_static {\n\talias /data/web_static/current/;\n\tautoindex off;\n}' /etc/nginx/sites-available/default
service nginx restart
