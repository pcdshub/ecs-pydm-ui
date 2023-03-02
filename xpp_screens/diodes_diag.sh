#!/bin/bash

source pcds_conda
export PYTHONPATH="/cds/home/e/espov/.local/lib/python3.9/site-packages:${PYTHONPATH}"

export MYDIR=`dirname $(readlink -f $0)` # gets script working dir

SCRIPT=$(basename "$0")
SCRIPT=${SCRIPT%%.*}

cd $MYDIR

echo "Launching ${SCRIPT}.ui"
pydm --hide-nav-bar $MYDIR/$SCRIPT.ui
