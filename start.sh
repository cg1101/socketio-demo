#!/bin/bash

DIR=${0%/*}
VERSION=${1:-2}

VENV=venv${VERSION}

if [ ! -e "${DIR}/${VENV}" ]; then
	if [ "${VERSION:0:1}" = "2" ]; then
		VENV=$(echo venv2.?)
	else
		VENV=$(echo venv3.?)
	fi
fi

cd "$DIR"
. ${VENV}/bin/activate
python manage.py run #server
