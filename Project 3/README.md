## Log Analysis Project: Reporting Tool
by Mostafa Elsheikh, in fulfillment of Udacity's <i class="icon-cog"></i> **[Full Stack Web Developer Nanodegree](https://www.udacity.com/course/nd004)**

### About

News is `PostgreSQL` database has 3 tables (Authors, Articles, Log). The log table is relatively massive (1,677,735 rows!).
Used simplified queries as I could, and preprocessed data through `SQL` queries rather than handling them through `Python` for much performance.

Reporting Tool answers 3 questions:
* What are the most popular three articles of all time?
* Who are the most popular article author of all time?
* On which days did more than 1% of request lead to errors?

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

To execute the program, run `python3 log_analysis.py` from the command line.