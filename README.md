[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Build Status](https://travis-ci.org/muhumuzab/MyDiary-API.svg?branch=develop)](https://travis-ci.org/muhumuzab/MyDiary-API) [![Coverage Status](https://coveralls.io/repos/github/muhumuzab/MyDiary-API/badge.svg?branch=develop)](https://coveralls.io/github/muhumuzab/MyDiary-API?branch=develop)

# Introduction

* **My Diary** is an online journal where users can pen down their thoughts and feelings.  

# Features

* Users can create an account and log in. 
* Users can view all entries to their diary. 
* Users can view the contents of a diary entry. 
* Users can add or modify an entry. 
  
# API Endpoints

|  Endpoints | Description  | Public Access |
| --- | :--- | ---: |
| POST  `/api/v1/login`  | logs in  a user. | TRUE
| POST  `/api/v1/register`  | registers a new user | TRUE
| POST  `/api/v1/entries/`  | Add a diary entry.| TRUE
| GET  `/api/v1/entries/`   | gets all diary entries.| TRUE
| GET  `/api/v1/entries/<diary_id>`  | Get diary entry by id. | TRUE
| PUT  `/api/v1/entries/<diary_id>`  | Update diary entry by id. | TRUE


# Dependencies

* This app functionality depends on multiple python packages including;
* click==6.7
* Flask==1.0.2
* Flask-API==1.0
* Flask-Testing==0.7.1
* itsdangerous==0.24
* Jinja2==2.10
* MarkupSafe==1.0
* validate-email==1.3
* Werkzeug==0.14.1
* pytest==3.6.3

# Installation
To run this project, you'll need a working installation of python 3 and pip3. You also may need virtualenv.

## To install the app:
1. Clone this repository - git clone https://github.com/muhumuzab/MyDiary-API/tree/develop
2. Make a virtual environment for the project - virtualenv /path/to/my-project-venv
3. Activate the virtual environment - source /path/to/my-project-venv/bin/activate
4. Install requirements - pip3 install requirements.txt
5. Navigate to the project root and run the tests.
-  type - pytest 
- All tests should be passing.
6. Navigate to the project root and run the app.py file.
- python app.py



# Testing
1. Install pytest extension.pip3 install pytest
2. Navigate to the root of the project.
3. Run pytest
- All tests should be passing.

