# Personal Website

A website created in Django as a personal project for storing personal information (resume/cv, about page), blogs, and a quasi-portfolio of work. Mostly, this exists just for me to gain familiarity with Django, but also as a tool for hosting blogs and other applications I would like to create for myself. Essentially, it's just my personal site for conducting business and sharing my skills and information with the world.

# Setting up virtual environment for Python development

`python -m venv [virtual-environment-dir]`

# Running virtual environment

`source [virtual-environment-dir]/bin/activate`

# Installing Django

`python3 -m pip install Django`

# Installing Postgres on Ubuntu/Pop-OS

## Installing Postgres

`sudo apt install postgresql`

## Setting up new role

First, login as postgres user

`sudo -i -u postgres`

Then, run create a new db user/role and follow prompts

`createuser --interactive`

## Create databases for role and site

As postgres account, run:

`createdb [role]`
`createdb [site-db]`

# Set Up

Navigate to directory where project should be created, and create project with the following script.

`django-admin startproject personal_website .`

Add the apps

`python manage.py startapp blog`

# Run Server

`python manage.py runserver`

# Notes for Production

Make sure to install Apache and mod_wsgi. See Django docs on installing Django
