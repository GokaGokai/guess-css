#! /bin/bash

for TRANS in scrapped-html/*
do
    NAME=$(echo $TRANS | cut -d '/' -f2 | cut -d '.' -f1)
    python3 transf.py $NAME
    echo Trans $NAME
done
echo "Done"