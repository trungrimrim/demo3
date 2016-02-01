Provisioning & new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualevn

eg, on Ubuntu:
    
   sudo apt-get install nginx git python3 python3-pip
   sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with , eg, staging.my-domain.com
* sed "s/SITENAME/hostToDeploy/g" nginx.template.conf | sudo tee /etc/nginx/sites-available/hostToDeploy
* (fix username as neccessary)
* symbolic linking: sudo ln -s ../sites-available/hostToDeploy /etc/nginx/sites-enabled/hostToDeploy
* (delete default site as neccessary)

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with , eg, staging.my-domain.com
* sed "s/SITENAME/hostToDeploy/g" gunicorn-upstart.template.conf | sudo tee /etc/init/hostToDeploy.conf

## Run services
* sudo service nginx reload
* sudo start hostToDeploy

## Folder structure:
Assume we have a user account at /home/ubuntu

/home/ubuntu/
            /sites
                    /SITENAME/
                                database
                                source
                                static
                                virtualenv

