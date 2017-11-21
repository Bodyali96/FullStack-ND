## Log Analysis Project: Reporting Tool
by Mostafa Elsheikh, in fulfillment of Udacity's <i class="icon-cog"></i> **[Full Stack Web Developer Nanodegree](https://www.udacity.com/course/nd004)**
### About
You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

#### Prerequisites
* Python 3
* [VirtualBox](virtualbox.org)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* PowerShell or Bash

#### Install Vagrant
Download: https://www.vagrantup.com/downloads.html

**Windows users:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

If Vagrant is successfully installed, you will be able to run `vagrant --version`
in your terminal to see the version number.

#### Download VM configuration

You can download and unzip file https://github.com/Sasa94s/FullStack-ND/archive/master.zip, will be located in folder `Project 3`. or you can clone repository using git command `git clone https://github.com/Sasa94s/FullStack-ND.git`

### How To Run

If you need to bring the virtual machine back online (with `vagrant up`), do so now. Then log into it with `vagrant ssh`.

Change your directory to `cd /vagrant/Backup/`, unzip `newsdata.zip` archive then load the data using this command `psql -d news -f newsdata.sql`

To execute the program, run `python3 newsdata.py` from the command line.