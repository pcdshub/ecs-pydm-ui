#!/bin/bash

cd /cds/group/pcds/epics/screens/edm/xpp/R0.3.0
edm -eolc -x -m "DEV=XPP:XCS:TCT:01" ls336Screens/lakeshore336.edl
#edm -eolc -x -m "DEV=$1" ls336Screens/lakeshore336.edl
