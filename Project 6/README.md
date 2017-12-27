# Linux Server Configuration Project

A baseline installation of Ubuntu Linux on a virtual machine to host a Flask web application. This includes the installation of updates, securing the system from a number of attack vectors and installing/configuring web and database servers.

### Get your Server

Start a new Ubuntu Linux server instance on [Amazon Lightsail](https://lightsail.aws.amazon.com/).

### Connect to your Server using SSH

* Create a directory.
        
        mkdir -p ~/.ssh

* Move the downloaded `.pem` file to `.ssh` directory we just created.
    
        mv key.pem ~/.ssh
    
        sudo chmod 400 ~/.ssh/key.pem

* Connect to instance.

        ssh -i ~/.ssh/key.pem ubuntu@54.212.247.55

### Update all currently installed packages

        sudo apt-get update
        sudo apt-get upgrade

### Change the SSH port from 22 to 2200

* Edit `sshd_config` file using `GNU Nano`.

      sudo nano /etc/ssh/sshd_config

* Change line #5 from `22` to `2200`.

* Restart SSH service.

      sudo service ssh restart



### Configure the Uncomplicated Firewall (UFW)

* Allow incoming connections for SSH (port 2200)

      sudo ufw allow 2200/tcp

* Allow incoming connections for HTTP (port 80)

      sudo ufw allow 80/tcp

* Allow incoming connections for NTP (port 123)

      sudo ufw allow 123/tcp

* Enable UFW

      sudo ufw enable

### Create a new user account named grader

      sudo adduser grader

### Give grader the permission to sudo

* Super user configuration

      sudo nano /etc/sudoers.d/grader

* *OR run the following*

      sudo visudo

* Add the following.

      grader ALL=(ALL) NOPASSWD:ALL 

### Create an SSH key pair for grader using the ssh-keygen tool

      ssh-keygen -t rsa

* Move generated key

      sudo su - grader
      mkdir .ssh
      touch .ssh/authorized_keys
      mv grader_key ~/.ssh/

* Move content of `grader_key.pub` to that of `authorized_keys`

      mv grader_key.pub  ~/.ssh/authorized_keys
      sudo chmod 700 .ssh
      sudo chmod 644 .ssh/authorized_keys 

* Connect to grader

      ssh -i ~/.ssh/grader_key grader@54.212.247.55 -p 2200

### Configure the local timezone to UTC.

      sudo dpkg-reconfigure tzdata
    
* Choose `None of the above`.
* Choose `UTC`

### Install and configure Apache to serve a Python mod_wsgi application.

* Install Apache2.

      sudo apt-get install apache2

* Install mod_wsgi.

      sudo apt-get install libapache2-mod-wsgi-py3

* Check whether mod_wsgi is enabled.

      sudo a2enmod wsgi

### Install and configure PostgreSQL.

      sudo apt-get install postgresql

* Switch to `postgres`, PostgreSQL User.

      sudo su - postgres
    
* Connect to your own database

      psql
    
* Create database user named `catalog`.

      CREATE ROLE catalog WITH LOGIN;
    
* Limit permissions of user.

      ALTER ROLE catalog CREATEDB;

* Set user `catalog` password

      \password catalog
          
* Exit `psql` by pressing `Ctrl+D`
* Switch back to `ubuntu` user by running `exit`

--------

### Install Git

      sudo apt-get install git

* Change directory
      
      cd /var/www

* Clone Item Catalog project repository

      sudo git clone https://github.com/Sasa94s/catalog.git

* Change ownership of `catalog` directory to ubuntu user

      sudo chown -R ubuntu:ubuntu catalog/

### Deploying Item Catalog Project

* Change current directory to project directory

      cd catalog

* Create `catalog.wsgi` file using `GNU Nano`

      sudo nano catalog.wsgi

* Add the following into the file created

      #!/usr/bin/python3
      import sys
      sys.stdout = sys.stderr

      activate_this = '/var/www/catalog/env/bin/activate_this.py'
      with open(activate_this) as file_:
      exec(file_.read(), dict(__file__=activate_this))

      sys.path.insert(0,"/var/www/catalog")

      from __init__ import app as application

* Install Python 3

      sudo apt-get install python3-pip

* Install Virtual Enviroment

      sudo -H pip3 install virtualenv

* Change current directory to `catalog` directory
      
      cd catalog/

* Create virtual enviroment called `env`

      virtualenv env

* Activate `env` virtual enviroment

      source env/bin/activate

* Install dependencies

      pip3 install httplib2
      pip3 install requests
      pip3 install --upgrade oauth2client
      pip3 install sqlalchemy
      pip3 install flask
      pip3 install psycopg2

* Run `__init__.py` main project file

      python3 __init__.py

* Check If you are getting this message when you're running the file

      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

* Configure Apache Server by editing `000-default.conf` file

      sudo nano /etc/apache2/sites-enabled/000-default.conf

* Add the following to `000-default.conf` file

      <VirtualHost *:80>
                  ServerName 54.212.247.55
                  ServerAdmin abdelaleem@gmx.com
                  WSGIScriptAlias / /var/www/catalog/catalog.wsgi
                  <Directory /var/www/catalog/>
                        Order allow,deny
                        Allow from all
                        Options -Indexes
                  </Directory>
                  Alias /static /var/www/catalog/static
                  <Directory /var/www/catalog/static/>
                        Order allow,deny
                        Allow from all
                        Options -Indexes
                  </Directory>
                  ErrorLog ${APACHE_LOG_DIR}/error.log
                  LogLevel warn
                  CustomLog ${APACHE_LOG_DIR}/access.log combined
      </VirtualHost>

* Reload Apache Server

      sudo service apahce2 reload

* Activate `env` virtual enviroment

      source env/bin/activate

* Run `database_setup.py`

      python3 database_setup.py

* Deactivate `env` virtual enviroment

      deactivate

* Restart Apache Server

      sudo service apache2 restart

* Go to http://54.212.247.55/

Resources:

* [Configuring Linux Web Servers](https://www.udacity.com/course/configuring-linux-web-servers--ud299)
* [Configuration Handling](http://flask.pocoo.org/docs/0.12/config/)
* [An Introduction to Linux Permissions](https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-permissions)
* [mod_wsgi (Apache) - Flask Documentation](http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/)
* [Apache Server Configuration Files](https://httpd.apache.org/docs/current/configuring.html)
* [Deploy a Flask Application on an Ubuntu VPS](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)
* [Viewing Apache Log files](https://www.a2hosting.com/kb/developer-corner/apache-web-server/viewing-apache-log-files)
