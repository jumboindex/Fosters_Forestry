# Flexbox - company website

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [To-do list](#to-do-list)
* [Status](#status)
 
## General info
 
This is a company website for my freind who is a tree surgeon, and created to practise using flexbox / responsive design. I have got a bit carried away, and set up a Flask server so I can grab the form data and email it to myself / sales@fostersforestry.co.uk if in production. At this stage I don't plan to purchase the domain name or set up a mail server / use forwarding. 

Orginally the form emailed any data sumbited to my gmail, however Flask throws an error when SMTPlib is unable to login to the mail server, so this sections was commented out and obviously i'm not going to upload passwords.
 
## Technologies
* HTML
* CSS
* Python 3
 
## Setup
```
pip install flask
```
## To-do list:
* create hamburger menu using JS.
* find a better way to store credentials to use SMTPlib.
 
## Status
Project is: _in progress_