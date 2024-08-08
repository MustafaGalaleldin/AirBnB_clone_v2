#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

# Install Nginx if it not already installed
if [[ ! -e /etc/nginx ]]; then
        sudo apt-get -y update
        sudo apt-get -y install nginx
        sudo service nginx start
fi

# Create the folder /data/ if it doesn’t already exist
sudo mkdir -p /data/

# Create the folder /data/web_static/ if it doesn’t already exist
sudo mkdir -p /data/web_static/

# Create the folder /data/web_static/releases/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/

# Create the folder /data/web_static/shared/ if it doesn’t already exist
sudo mkdir -p /data/web_static/shared/

# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/test/

# Create a fake HTML file /data/web_static/releases/test/index.html
echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>TATAKAE</p>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
# If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group Recursively
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
add="\tlocation /hbnb_static {\n\t\talias /data/web_static/current/index.html;\n\t}"
sudo sed -i "/server_name _;/a \\$add" /etc/nginx/sites-available/default
