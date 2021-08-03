# Flexbox - company website

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [To-do list](#to-do-list)
* [Status](#status)
 
## General info
 
This is a company website for my freind who is a tree surgeon, and was created to practise using flexbox. I have got a bit carried away, and set up a Flask server so I can grab the form data and email it to myself / sales@ if in production. 

Orginally the form emailed any data sumbited to my gmail, however I have commented out the SMTPlib email section due to security concerns (passwords), and flask breaks when SMTPlib throws an error.
 
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