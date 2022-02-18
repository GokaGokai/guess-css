#!/bin/bash

# REPINPUT=$1
# REPOUTPUT=$2

REPINPUT="scrapped-html"
REPOUTPUT="transf-html"

mkdir $REPOUTPUT

for TRANS in $REPINPUT/*
do
    NAME=$(echo $TRANS | cut -d '/' -f2 | cut -d '.' -f1)
    python3 transf.py $REPINPUT $REPOUTPUT $NAME
    echo Trans $NAME
done

mkdir $REPOUTPUT/css
cp skeleton-html/css/main.css $REPOUTPUT/css

echo "Done"

# ---
# Back up
# ---
# for TRANS in scrapped-html/*
# do
#     NAME=$(echo $TRANS | cut -d '/' -f2 | cut -d '.' -f1)
#     python3 transf.py $NAME
#     echo Trans $NAME
# done
# echo "Done"