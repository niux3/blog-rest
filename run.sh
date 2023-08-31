#!/bin/bash

if [ ! -d ".venv" ]
    then
        mkdir .venv && pipenv shell && pipenv install -r Pipfile
    else
        pipenv shell 
fi
export FLASK_ENV=development && export FLASK_APP=app && flask run -p 8000

