# Item Catalog Project: CATALOG
by Mostafa Elsheikh, in fulfillment of Udacity's <i class="icon-cog"></i> **[Full Stack Web Developer Nanodegree](https://www.udacity.com/course/nd004)**

## About

A dynamic website developed by `Python Flask Framework` with persistent data storage `SQLite Database` to create a web application that provides a compelling service to users.
It provides features using HTTP methods for registered users for `SQLAlchemy` CRUD operations (creating, reading, updating, deleting) on data. 
Implementing third-party OAuth authentication system provided by Google. 

## Getting Started

#### Prerequisites
* [Python 3](https://www.python.org/ftp/python/3.6.3/python-3.6.3.exe)
* [VirtualBox](virtualbox.org)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* PowerShell or Bash Terminal

#### Install Vagrant
Download: https://www.vagrantup.com/downloads.html

**Windows users:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

If Vagrant is successfully installed, you will be able to run `vagrant --version`
in your terminal to see the version number.

#### VM configuration

You don't need to download configuration as it's provided in project folder: `Vagrantfile`.

### How To Run

If you need to bring the virtual machine back online (with `vagrant up`), do so now. Then log into it with `vagrant ssh`.

Change your directory to `cd /vagrant/`

To execute the program, run `python3 project.py` from the command line.

## Preview

### Home Page

The homepage displays all current categories along with the latest added items.

http://localhost:8000

![Home Page](https://github.com/Sasa94s/FullStack-ND/blob/master/Project%204/Preview/Screen01.png)

### Show Category Items

Selecting a specific category shows you all the items available for that category.

http://localhost:8000/catalog/Soccer/Items

![Show Category Items](https://github.com/Sasa94s/FullStack-ND/blob/master/Project%204/Preview/Screen02.png)


### Show Item

Selecting a specific item shows you specific information of that item.

http://localhost:8000/catalog/Soccer/Footwear

![Show Item](https://github.com/Sasa94s/FullStack-ND/blob/master/Project%204/Preview/Screen03.png)


### Search

Finding Items by text between words

http://localhost:8000/catalog/find

![Search](https://github.com/Sasa94s/FullStack-ND/blob/master/Project%204/Preview/Screen05.png)



### Add New Item

http://localhost:8000/catalog/item/new

![Add New Item](https://github.com/Sasa94s/FullStack-ND/blob/master/Project%204/Preview/Screen07.png)


### Edit

http://localhost:8000/catalog/Hockey/Stick/edit

![Edit](https://github.com/Sasa94s/FullStack-ND/blob/master/Project%204/Preview/Screen06.png)


### Delete

http://localhost:8000/catalog/Hockey/Stick/delete

![Delete](https://github.com/Sasa94s/FullStack-ND/blob/master/Project%204/Preview/Screen08.png)


### Login Page

http://localhost:8000/login

![Login](https://github.com/Sasa94s/FullStack-ND/blob/master/Project%204/Preview/Screen04.png)


### JSON Endpoint

http://localhost:8000/catalog/JSON

![Login](https://github.com/Sasa94s/FullStack-ND/blob/master/Project%204/Preview/Screen09.png)

