#!/bin/bash

FILE_DIR=$(dirname ${BASH_SOURCE})

ENV=${FILE_DIR}/env
if [ -e "$ENV" ]; then
	. $ENV
fi

ALIASES=${FILE_DIR}/.aliases
if [ -e "$ALIASES" ]; then
	. ${ALIASES}
fi

PYTHONSTART=${FILE_DIR}/.pythonstart
if [ -e "$PYTHONSTART" ]; then
	export PYTHONSTARTUP="${PYTHONSTART}"
fi
