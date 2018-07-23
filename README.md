# log-analysis
This projects was proprosed by udacity, in order to improve knowledge in database.
It is a database with three tables, they are: articles, authors and log. The information extracted from the database is:
1. What are the three most popular articles of all time?
2. Who are the authors of most popular articles of all time?
3. In which days more than 1% of requests resulted in errors?

## To run

### Required Programs 
 - Python
 - PostgreSQL
 - VirtualBox
 - Vagrant

### Setup
 - Install VirtualBox and Vagrant
 - Configure a VM with PostgreSQL and Python
 - Clone this project

### To run
 - Launch vagrant vm by running 'vagrant up', log in with 'vagrant ssh'
 - Load the data with 'psql -d news -f newsdata.sql'
 - In a command line run 'python newsdata.py'
 - Check the log file LogAnalysis