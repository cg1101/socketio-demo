#!/bin/bash

DIR=${0%/*}
VERSION=${1:-2}

VENV=venv${VERSION}

if [ ! -e "${DIR}/${VENV}" ]; then
	if [ "${VERSION:0:1}" = "2" ]; then
		VENV=venv2.7
	else
		VENV=venv3.5
	fi
fi

cd "$DIR"
. ${VENV}/bin/activate
python manage.py run #server
