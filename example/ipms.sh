#!/bin/bash

source pcds_conda

export MYDIR=`dirname $(readlink -f $0)` # gets script working dir

SCRIPT=$(basename "$0")
SCRIPT=${SCRIPT%%.*}

echo "Launching ${SCRIPT}.ui"
pydm $MYDIR/$SCRIPT.ui
